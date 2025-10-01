import copy
import pickle
from dataclasses import dataclass
from enum import Enum
from logging import Logger
from pathlib import Path
from string import Template
from typing import List, Sequence, Optional, Collection

import networkx as nx
from attrs import define, field

from amberflow.pipeline import Pipeline
from amberflow.execution import BaseCommand
from amberflow.worknodes import BaseWorkNode, WorkNodeStatus

__all__ = ("BatchStatus", "Batch", "BatchCommand", "create_batch_commands", "split_pipeline")


class BatchStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


@dataclass(frozen=False)
class Batch:
    id: str
    status: BatchStatus
    systems: Collection[str]
    pipeline: Pipeline
    state: dict
    pickle_filename: str
    checkpoint_filename: str


@define
class BatchCommand:
    command: BaseCommand = field(validator=lambda self, attr, value: isinstance(value, BaseCommand))
    command_template: Template = field(default=Template("runflow $PICKLE_PATH"))
    command_str: Optional[str] = field(default=None)
    batch: Optional[Batch] = field(default=None)
    remote_server: str = field(init=False)
    remote_base_dir: Path = field(init=False)
    local_base_dir: Path = field(init=False)
    keyfile: Optional[Path] = field(init=False, default=None)
    exclude_when_downloading: Collection[str] = field(init=False, default=("*.nc",))

    def __attrs_post_init__(self):
        self.remote_server = self.command.executor.remote_server
        self.remote_base_dir = Path(self.command.executor.remote_base_dir)
        self.local_base_dir = Path(self.command.executor.local_base_dir)
        self.keyfile = Path(self.command.executor.keyfile) if self.command.executor.keyfile is not None else None

    def test_connection(self, logger: Logger, timeout: int = 5) -> bool:
        return self.command.executor.test_connection(logger=logger, timeout=timeout)

    def attach_batch(self, batch: Batch, logger: Logger) -> None:
        batch.pipeline.setup_new_cwd(remote_base_dir=self.remote_base_dir)
        self.batch = batch
        with open(Path(self.local_base_dir, batch.pickle_filename), "wb") as f:
            # noinspection PyTypeChecker
            pickle.dump(batch.pipeline, f)
        pickle_path = Path(self.remote_base_dir, batch.pickle_filename)
        self.command_str = self.command_template.substitute(PICKLE_PATH=str(pickle_path))
        logger.info(f"Attached batch {batch.id} with systems {batch.systems} to command for {self.remote_server}.")

    def sync_batch(self, logger: Logger) -> bool:
        """
        TODO: sometimes, if the rmeote batch is not identical to the local, you want to return False
        """
        executor = getattr(self.command, "executor")
        if executor.exists(Path(self.local_base_dir, self.batch.checkpoint_filename), logger):
            cpt = executor.download(Path(self.local_base_dir, self.batch.checkpoint_filename), logger)
        else:
            # No checkpoint on remote, so nothing to sync
            return False

        state = self.batch.pipeline.read_state_from_checkpoint(cpt)
        last_node, done = self.find_current_node(state["flow"])
        # Update the local pipeline state with the downloaded checkpoint state. If the remote checkpoint is older,
        # (lacks nodes), then it definitely isn't finished, even if all nodes in it are completed.
        is_newer = self.batch.pipeline.sync_state_if_newer(state)
        done = done and is_newer

        if last_node.status == WorkNodeStatus.FAILED:
            last_node_work_dir = getattr(last_node, "work_dir")
            if last_node_work_dir is None:
                err_msg = f"Node {last_node.id} from batch {self.batch.id} has no work_dir set, cannot download."
                logger.error(err_msg)
            else:
                failed_node_dir = executor.download(last_node_work_dir, logger, exclude=self.exclude_when_downloading)
                logger.error(f"{last_node.id} failed. Downloaded its `work_dir` at: {failed_node_dir}")
                return True
        if done:
            assert last_node.status == WorkNodeStatus.COMPLETED, "If done is True, last_node must be COMPLETED"
            self.batch.status = BatchStatus.COMPLETED
            for leaf_node in self.batch.pipeline.leafs:
                for sys in self.batch.systems:
                    dirname = Path(self.local_base_dir, sys, leaf_node.out_dirname)
                    self.command.executor.download(dirname, logger, is_dir=True)

        # The remote checkpoint may show all nodes as completed, but there are still more nodes to run in the
        # local version of the pipeline. We'll mark the batch as pending so the new pickled pipeline gets
        # uploaded, so it runs the new nodes and updates the checkpoint again.

        return done

    def run(self, logger: Logger):
        logger.info(f"Batch {self.batch.id} with systems {self.batch.systems} is {self.batch.status.value}.")
        local_pickle_path = Path(self.local_base_dir, self.batch.pickle_filename)
        executor = getattr(self.command, "executor")
        executor.upload(local_pickle_path, logger)

        starting_nodes = self.find_parents_of_first_uncompleted_nodes(self.batch.pipeline.flow)
        for sys in self.batch.systems:
            for node in starting_nodes:
                wn_dirpath = Path(self.local_base_dir, sys, node.out_dirname)
                executor.upload(wn_dirpath, logger, mkdir=True)

        self.command.run(
            [self.command_str],
            cwd=self.local_base_dir,
            logger=logger,
            upload=False,
            download=False,
        )
        self.batch.status = BatchStatus.RUNNING
        logger.info(f"Batch {self.batch.id} with systems {self.batch.systems} is {self.batch.status.value}.")

    @staticmethod
    def find_current_node(dag: nx.DiGraph) -> tuple[BaseWorkNode, bool]:
        """
        Finds the first node in a DAG that is not completed and returns it.


        Args:
            dag: The directed acyclic graph (DAG) of WorkNode objects.

        Returns:

        """
        # Iterate through the graph in an order that respects dependencies
        node = next(iter(dag.nodes))
        for node in nx.topological_sort(dag):
            if node.status == WorkNodeStatus.COMPLETED:
                continue
            elif node.status == WorkNodeStatus.FAILED:
                return node, True
            elif node.status in {WorkNodeStatus.RUNNING, WorkNodeStatus.PENDING}:
                return node, False

        return node, True

    @staticmethod
    def find_parents_of_first_uncompleted_nodes(dag: nx.DiGraph) -> List[BaseWorkNode]:
        """
        Finds the first node(s) in a DAG that are not completed and returns their parents.

        This function identifies the "frontier" of the DAG—the set of nodes that
        are not yet completed but all of their direct parents are. It then returns
        a unique list of those parents.

        Args:
            dag: The directed acyclic graph (DAG) of WorkNode objects.

        Returns:
            A list of the parent WorkNode objects for the first uncompleted nodes.
        """
        first_uncompleted_nodes: List[BaseWorkNode] = []

        # Iterate through the graph in an order that respects dependencies
        for node in nx.topological_sort(dag):
            if node.status != WorkNodeStatus.COMPLETED:
                # An uncompleted node is part of the "frontier" if all its
                # parents are completed.
                parents = list(dag.predecessors(node))
                if all(p.status == WorkNodeStatus.COMPLETED for p in parents):
                    first_uncompleted_nodes.append(node)

        # Collect all unique parents of the frontier nodes
        parent_nodes: set[BaseWorkNode] = set()
        for node in first_uncompleted_nodes:
            parent_nodes.update(dag.predecessors(node))

        return list(parent_nodes)


def create_batch_commands(
    base_command: BaseCommand, servers: Sequence[str], *, command_template: Optional[Template] = None
) -> list[BatchCommand]:
    """
    Factory to create a list of BatchCommands from a template command and a list of remote addresses.

    Args:
        base_command: The command object to use as a template.
        servers: list of user@server strings.
        command_template: An optional Template object to format the command string. If None, a default template is used.

    Returns:
        A list of configured BatchCommand instances.
    """
    if command_template is None:
        command_template = Template("source /home/ubuntu/flowrc && runflow $PICKLE_PATH")
    commands = []
    for remote_server in servers:
        # cmd_instance = copy.deepcopy(base_command)
        # setattr(cmd_instance, "remote_server", remote_server)
        # commands.append(BatchCommand(command=cmd_instance))
        cmd_instance = base_command.replace(remote_server=remote_server)
        commands.append(BatchCommand(command=cmd_instance, command_template=command_template))

    return commands


def split_pipeline(pipeline: Pipeline, batch_systems: Collection[str], new_name: str) -> Pipeline:
    """
    Splits a Pipeline into n_batches smaller Pipelines.

    Args:
        pipeline: The original Pipeline to split.
        batch_systems: A subselection of system names to include in the new Pipeline.
        new_name: The new name will re-set the checkpoint, pickle and logger filenames

    Returns:
        A list of Pipeline instances.
    """
    if len(batch_systems) < 1:
        raise ValueError("batch_systems must be at least 1")

    other_pipeline = copy.deepcopy(pipeline)
    other_pipeline.rename(new_name)

    # First, filter the systems
    other_pipeline.systems = {
        sysname: sysdir for sysname, sysdir in pipeline.systems.items() if sysname in batch_systems
    }
    if len(other_pipeline.systems) == 0:
        raise ValueError("No valid systems found in the provided batch_systems")

    # Also filter them on each node
    for node in other_pipeline.flow.nodes:
        node.set_systems(batch_systems)

    # The, filter the artifacts
    for batch_artifacts in other_pipeline.artifacts.values():
        batch_artifacts.only_systems(batch_systems)

    return other_pipeline
