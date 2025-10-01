import logging
import os
import pickle
import re
import subprocess as sp
from copy import deepcopy
from pathlib import Path
from typing import Sequence, Iterable, Optional, Any, Collection, Set

import networkx as nx
from attr import Converter, Factory
from attrs import define, field

from amberflow.artifacts import (
    TargetProteinPDB,
    ArtifactRegistry,
    BinderLigandPDB,
    BinderLigandSmiles,
    BaseComplexStructureFile,
    BatchArtifacts,
    BaseArtifact,
    ArtifactContainer,
    PipelineArtifacts,
)
from amberflow.checkpoint import PipelineCheckpointer
from amberflow.flows import BaseFlow
from amberflow.primitives import (
    InvalidPipeline,
    UnknownFileType,
    DirHandle,
    conv_build_resnames_set,
    set_logger,
    UnknownArtifactError,
    dirpath_t,
    filepath_t,
)
from amberflow.schedulers import BaseScheduler
from amberflow.worknodes import BaseWorkNode, WorkNodeDummy, WorkNodeStatus, draw_flow_graph

__all__ = ["Pipeline"]


@define
class Pipeline:
    """
    The main orchestrator for an amberflow simulation workflow.

    This class discovers input data, builds a computational graph of work nodes,
    and uses a scheduler to execute the defined pipeline. It handles checkpointingdef
    to allow for resuming interrupted workflows.

    Attributes
    ----------
    name : str
        The name of the pipeline.
    cwd : dirpath_t
        The current working directory where systems are located and outputs will be generated.
    target : str
        The name assigned to the target molecule type, typically 'protein' or 'na'.
    binder : str
        The name assigned to the binder molecule type, typically 'ligand'.
    scheduler : BaseScheduler
        The scheduler instance responsible for executing the work nodes.
    new_run : bool
        Flag indicating if this is a new run (True) or a resumed run (False).
    ignore_checkpoint : bool
        If True, forces a new run, ignoring any existing checkpoint file.
    force_restart : bool
        If True, ignores checkpoint validation errors and starts fresh.
    pickle_filename: str
        The name of the pickle file used for serialization.
    logger : logging.Logger
        The logger for the pipeline.
    logging_level : int
        The logging level.
    systems : dict[str, dirpath_t]
        A dictionary mapping system names to their respective directory paths.
    root : WorkNodeDummy
        The root node of the workflow graph.
    leafs : list[BaseWorkNode]
        The leaf nodes of the workflow graph.
    free_md : bool
        If True, allows running simulations without a complex structure.
    user_accepted_resnames : set
        A set of user-provided residue names to be accepted.
    flow : nx.DiGraph
        The NetworkX directed graph representing the workflow.
    flow_ids : set[str]
        A set of all work node IDs in the flow.
    artifacts : PipelineArtifacts
        A dictionary storing all artifacts generated during the pipeline execution.
    rootid : str
        The identifier for the root node.
    """

    name: str = field(converter=str)
    cwd: dirpath_t = field(kw_only=True, converter=lambda value: Path(value).resolve())
    only_systems: Optional[Collection[str]] = field(kw_only=True, default=None)
    target: str = field(kw_only=True, converter=str, default="protein")
    binder: str = field(kw_only=True, converter=str, default="ligand")
    scheduler: BaseScheduler = field(kw_only=True)
    new_run: bool = field(default=True)
    ignore_checkpoint: bool = field(default=False)
    validate_checkpoint: bool = field(default=True)
    force_restart: bool = field(default=False)
    pickle_filename: str = field(init=False)
    logger_filename: str = field(init=False)
    logger: logging.Logger = field(init=False, default=None)
    logging_level: int = field(kw_only=True, default=logging.INFO)
    systems: dict[str, dirpath_t] = field(init=False, default=Factory(dict))
    root: WorkNodeDummy = field(init=False)
    leafs: list[BaseWorkNode] = field(init=False)
    free_md: bool = field(init=True, default=True)
    user_accepted_resnames: set = field(kw_only=True, converter=Converter(conv_build_resnames_set), default=None)
    flow: nx.DiGraph = field(init=False, default=Factory(nx.DiGraph))
    flow_ids: set[str] = field(init=False, default=Factory(set))
    artifacts: PipelineArtifacts = field(init=False, default=Factory(dict))
    checkpointer: PipelineCheckpointer = field(init=False)
    rootid = "Root"

    def __attrs_post_init__(self):
        """
        Initialize the pipeline after all attributes have been set.

        This method serves as the main entry point for setting up the pipeline,
        handling both new runs and continuations from a checkpoint. It discovers
        input systems and their initial artifacts, and sets up the root node of the
        workflow graph.
        """
        self.checkpointer = PipelineCheckpointer(
            f"cpt_{self.name}.pkl",
            tracked_obj=self,
            checkpoint_path=Path(self.cwd, f"cpt_{self.name}.pkl"),
            ignore_checkpoint=self.ignore_checkpoint,
            force_restart=self.force_restart,
        )
        self.rename_pickle()
        self.rename_logger()
        self.logger = set_logger(
            Path(self.cwd, self.logger_filename),
            logging_level=self.logging_level,
            filemode="w" if self.checkpointer.new_run else "a",
        )
        # Get the root dir system and the starting artifacts to pipe them through the root node.
        starting_artifacts, self.systems = self._walk_main_dir(self.only_systems)
        root_artifacts = dict()
        # noinspection PyTypeChecker
        self.root = self._setup_new_node(WorkNodeDummy(wnid=self.rootid))
        for sysname, syspath in self.systems.items():
            self.logger.debug(f"Loading system {sysname}")
            self.root.run(starting_artifacts[sysname], sysname=sysname, cwd=syspath)
            root_artifacts[sysname] = self.root.output_artifacts
        # load them into the artifact tree's root.
        self.artifacts[self.rootid] = BatchArtifacts(self.rootid, root_artifacts)
        self.flow_ids.add(self.rootid)

        if self.checkpointer.new_run:
            self.flow = nx.DiGraph(name="workflow")
            self.flow.add_node(self.root)
            self.leafs = [self.root]
        else:
            self.checkpointer.load_and_set(self.systems, self.logger, validate=self.validate_checkpoint)
            # state = self.checkpointer.load(self.systems, self.logger, validate=self.validate_checkpoint)
            # self.flow, self.leafs, self.artifacts, self.systems = (
            #     state["flow"],
            #     state["leafs"],
            #     state["artifacts"],
            #     state["systems"],
            # )

    def rename(self, name: Optional[str] = None) -> None:
        self.name = self.name if name is None else name
        self.checkpointer.name = f"cpt_{self.name}.pkl"
        self.checkpointer.checkpoint_path = Path(self.cwd, self.checkpointer.name)
        self.rename_pickle()
        self.rename_logger()

    def rename_pickle(self) -> None:
        self.pickle_filename = f"{self.name}.pkl"

    def rename_logger(self) -> None:
        self.logger_filename = f"{self.name}.log"

    def _read_checkpoint(self, checkpoint_path: filepath_t, force_restart: bool) -> None:
        """
        Read and validate the workflow state from a checkpoint file.

        This method loads a previously saved pipeline state, including the
        workflow graph, artifacts, and system information. It then validates
        the state to ensure that all required files for completed nodes are
        present. Failed or canceled nodes are reset to a pending state to be
        re-run.

        Parameters
        ----------
        checkpoint_path : filepath_t
            The path to the checkpoint file.
        force_restart : bool
            If True, validation errors will be ignored, and the pipeline will
            attempt to continue. This can be useful for debugging but may lead
            to unexpected behavior.

        Raises
        ------
        InvalidPipeline
            If the checkpoint is found to be invalid and `force_restart` is False.
        """
        old_systems: dict[str, DirHandle] | None = None
        try:
            with open(checkpoint_path, "rb") as f:
                self.flow, self.artifacts, self.leafs, old_systems = pickle.load(f)
            self.new_run = False
        except FileNotFoundError:
            self.new_run = True
            return

        # Now, check if the systems in the checkpoint match the current systems.
        assert old_systems is not None, "Expected old_systems to be not None when validating checkpoint."
        set_old_systems = set(old_systems.keys())

        valid = True
        err_msg = ""
        is_root = True
        for node in nx.topological_sort(self.flow):
            if is_root:
                if node.id != self.rootid:
                    err_msg += f"Pipeline's root node id is {self.rootid}, but found {node.id}.\n"
                    valid = force_restart
                    break
                is_root = False
            if node.status in (WorkNodeStatus.FAILED, WorkNodeStatus.CANCELLED):
                node.status = WorkNodeStatus.PENDING
                continue
            elif node.status == WorkNodeStatus.COMPLETED:
                if wd := getattr(node, "work_dir", False):
                    if not wd.is_dir():
                        valid = force_restart
                        err_msg += f"WorkNode {node.id} has no work directory ({node.work_dir}).\n"
                        break
                    else:
                        valid = False
                        err_msg += f"WorkNode {node.id} has no work directory but is marked as completed?. Corrupted checkpoint file?"
                        break
                for _, art_list in node.output_artifacts.items():
                    for art in art_list:
                        if hasattr(node, "filepath"):
                            # artifact is file-based
                            if not art.filepath.is_file():
                                valid = False
                                err_msg += f"WorkNode {node.id} has no output artifact {art}.\n"
                                break

        for sysname in self.artifacts[self.rootid].keys():
            if sysname not in set_old_systems:
                self.logger.warning(f"Missing system in the current root dir: {sysname}")

        if not valid:
            err_msg += "Invalid Pipeline. Cannot continue from the checkpoint. Either set `force_restart=True`, or fix the project files."
            self.logger.error(err_msg)
            raise InvalidPipeline(err_msg)

        return

    def read_state_from_checkpoint(self, checkpoint_path: Optional[Path] = None) -> dict[str, Any]:
        """
        Load the pipeline state from the checkpoint file and return it.

        """
        return self.checkpointer.load(self.systems, self.logger, validate=False, checkpoint_path=checkpoint_path)

    def sync_flow(self, state_flow: nx.DiGraph) -> bool:
        """
        Synchronizes the 'status' attribute of nodes from a state graph to the self graph.


        Args:
            state_flow: A flow from a checkpoint.

        Returns:
            bool: True if the self graph's statuses were updated, False otherwise.

        Scenarios:
        1. Exact Match: If states and self have the exact same nodes and edges, the 'status' of each node in
            self_flow is updated from state_flow.
            Returns True.
        2. self is Newer: If the state graph is a strict subgraph of the self one (i.e., self has more nodes or edges),
            no action is taken.
            Returns False.
        3. state is Newer: If the state graph has any nodes or edges that do not exist in the self graph, the 'status'
            of each node in self_flow is updated from state_flow.
            Returns True.
        """
        state_nodes = set(state_flow.nodes)
        self_nodes = set(self.flow.nodes)
        state_edges = set(state_flow.edges)
        self_edges = set(self.flow.edges)

        # If self.flow has more nodes or edges, it's considered newer. Do nothing.
        state_is_subset = state_nodes.issubset(self_nodes) or state_edges.issubset(self_edges)
        self_is_subset = self_nodes.issubset(state_nodes) or self_edges.issubset(state_edges)

        if state_is_subset and self_is_subset:
            # Identical graphs, assuming state is newer
            for self_node, state_node in zip(self.flow.nodes, state_flow.nodes):
                assert self_node.id == state_node.id, (
                    f"Flow IDs do not match. This shouldn't happen. {self.flow.nodes=} != {state_flow.nodes=}"
                )
                self_node.status = state_node.status
            return True
        elif state_is_subset and not self_is_subset:
            # self is newer, do nothing
            return False
        elif not state_is_subset and self_is_subset:
            # state is newer, update statuses
            state_flow_nodes = {n.id: n.status for n in state_flow.nodes}
            for self_node in self.flow.nodes:
                self_node.status = state_flow_nodes[self_node.id]
            return True
        else:
            assert False, (
                f"Unexpected case in sync_flow(). This shouldn't happen. {self.flow.nodes=} --- {state_flow.nodes=}"
            )

    def sync_state_if_newer(self, state: dict[str, Any]) -> bool:
        """
        Synchronizes the pipeline's state with a given state dictionary, without assuming that the state is a one-to-one
        match with the current Pipeline.

        Args:
            state: A state from a checkpoint, tipically a state one.

        Returns:
            bool: True if the self graph's statuses were updated, False otherwise.
        """
        state_is_newer = self.sync_flow(state["flow"])
        # TODO: update artifacts, even if state_is_newer is False and the systems are not the same.
        if state_is_newer:
            for node_id, incoming_batch_arts in state["artifacts"].items():
                batch_artifacts = deepcopy(incoming_batch_arts)
                if node_id in self.artifacts:
                    self.artifacts[node_id].update_inplace(batch_artifacts)
                else:
                    self.artifacts[node_id] = batch_artifacts
                # The state may be remote, so we need to change the base dir of the artifacts to the current cwd.
                batch_artifacts.change_base_dir(state["cwd"], self.cwd)

        return state_is_newer

    def _walk_main_dir(self, only_systems: Set[str] = None) -> tuple[BatchArtifacts, dict[str, DirHandle]]:
        """
        Discover and collect initial artifacts from system directories.

        This method scans the main working directory (`cwd`) for subdirectories,
        each representing a unique system to be simulated. It collects the initial
        set of artifacts (e.g., PDB files) from each system directory.

        Returns
        -------
        tuple[BatchArtifacts, dict[str, DirHandle]]
            A tuple containing a batch of the initial artifacts for all discovered
            systems and a dictionary mapping system names to their directory paths.
        """
        artifacts: dict[str, ArtifactContainer] = {}
        systems: dict[str, DirHandle] = {}
        for path_object in Path(self.cwd).iterdir():
            if path_object.is_dir():
                if path_object.name.startswith("allow_") or path_object.name.startswith("__"):
                    continue
                if only_systems is not None and path_object.name not in only_systems:
                    continue
                sys_artifacts: ArtifactContainer = self._add_system_dir(path_object)
                artifacts[sys_artifacts.id] = sys_artifacts
                systems[sys_artifacts.id] = DirHandle(path_object)

        if len(systems) < 1:
            err_msg = f"No valid system directories found in {self.cwd}."
            self.logger.error(err_msg)
            raise InvalidPipeline(err_msg)

        return BatchArtifacts("Root", artifacts), systems

    def _add_system_dir(self, system_path: Path) -> ArtifactContainer:
        """
        Identify and register artifacts from a single system directory.

        This method scans a given system directory for files that match known
        artifact patterns (e.g., 'target_*.pdb', 'binder_*.sdf'). It creates
        and registers these files as the initial artifacts for the system.

        Parameters
        ----------
        system_path : Path
            The path to the system directory to be scanned.

        Returns
        -------
        ArtifactContainer
            A container holding all the artifacts discovered in the directory.

        Raises
        ------
        InvalidPipeline
            If the directory contains unrecognized files or an invalid combination
            of input files (e.g., multiple targets or binders).
        """
        has_complex: bool = False
        has_target: bool = False
        has_binder: bool = False
        artifacts: list[BaseArtifact] = []
        # The folder name is the system name.
        sysname = str(system_path.name)

        for file in Path(system_path).iterdir():
            if file.is_file():
                try:
                    # TODO: hacky. Can do better.
                    if file.name.startswith("target_"):
                        file_artifact = ArtifactRegistry.create_instance_by_filename(file, tags=(self.target,))
                    elif file.name.startswith("binder_"):
                        file_artifact = ArtifactRegistry.create_instance_by_filename(file, tags=(self.binder,))
                    elif file.name.startswith("complex_"):
                        file_artifact = ArtifactRegistry.create_instance_by_filename(
                            file, tags=(self.target, self.binder)
                        )
                    else:
                        file_artifact = ArtifactRegistry.create_instance_by_filename(file)

                    artifacts.append(file_artifact)
                    artifact_type = type(file_artifact)

                    if issubclass(artifact_type, BaseComplexStructureFile):
                        if has_complex:
                            raise InvalidPipeline(f"System dir {system_path} has multiple complexes.")
                        has_complex = True
                    if issubclass(artifact_type, TargetProteinPDB):
                        if has_target:
                            raise InvalidPipeline(f"System dir {system_path} has multiple targets.")
                        has_target = True
                    if issubclass(artifact_type, BinderLigandPDB) or issubclass(artifact_type, BinderLigandSmiles):
                        if has_binder:
                            raise InvalidPipeline(f"System dir {system_path} has multiple binders.")
                        has_binder = True
                except UnknownFileType:
                    raise InvalidPipeline(f"System dir {system_path} has an unrecognized file ({file}).")
                except UnknownArtifactError as e:
                    self.logger.debug(f"System dir {system_path} has an unrecognized file: {file} which caused {e}.")

        if self.free_md or has_complex or (has_target and has_binder):
            self.systems[sysname] = DirHandle(system_path)
            return ArtifactContainer(sysname, artifacts)
        else:
            raise InvalidPipeline(
                f"Invalid dir: {system_path}. "
                "Structures of target and binder (together or separate) are a prerequisite."
            )

    def launch(self) -> None:
        """
        Execute the pipeline directly in the current process.

        This method is primarily intended for debugging and testing purposes.
        For production runs, it is recommended to use the `run()` method to
        ensure a clean and isolated execution environment.
        """
        self.scheduler.launch(
            self.flow,
            self.root,
            systems=self.systems,
            cwd=Path(self.cwd),
            pipeline_artifacts=self.artifacts,
            logger=self.logger,
            checkpointer=self.checkpointer,
        )

    def setup_new_cwd(
        self,
        *,
        remote_base_dir: Path,
        systems_subset: Optional[Sequence[str]] = None,
    ) -> None:
        self.cwd, self.systems, self.artifacts, self.flow = change_cwd(
            cwd=self.cwd,
            new_cwd=remote_base_dir,
            systems=self.systems,
            artifacts=self.artifacts,
            flow=self.flow,
            checkpointer=self.checkpointer,
            systems_subset=systems_subset,
        )

    # TODO: this function will probably go away and be replaced by `split_pipeline()`+ `setup_new_cwd()`
    def setup_new_pipeline(
        self, *, remote_base_dir: Path, batch_systems: Sequence[str], new_checkpoint_filename: Optional[str] = None
    ) -> "Pipeline":
        """
        Prepare a deep copy of the pipeline for execution.

        This method creates a standalone, serializable copy of the pipeline
        that can be safely executed in a separate process.

        For remote execution, it also adjusts the `cwd` and artifact file paths
        within the new pipeline to point to their expected locations on the
        remote server.

        Parameters
        ----------
        remote_base_dir : Path
            Remote `cwd` for the pipeline
        batch_systems : Sequence[str]
            A sequence of system names to include in the new pipeline.
        new_checkpoint_filename : Optional[str]
            An optional new filename for the checkpoint file in the new pipeline.

        Returns
        -------
        Pipeline
            A new, deep-copied pipeline instance configured for execution.
        """
        other_pipeline = deepcopy(self)
        # Now, all paths need fixing
        other_pipeline.setup_new_cwd(remote_base_dir=remote_base_dir, systems_subset=batch_systems)
        if new_checkpoint_filename is not None:
            other_pipeline.checkpointer.checkpoint_path.with_name(new_checkpoint_filename)

        return other_pipeline

    def _setup_new_node(self, new_worknode: BaseWorkNode) -> BaseWorkNode:
        """
        Prepare a new work node for inclusion in the pipeline.

        This method configures a new work node with the necessary pipeline-level
        information, such as the list of systems, the root directory, and the
        logging level. It also checks for ID conflicts to prevent duplicate
        nodes in the workflow.

        Parameters
        ----------
        new_worknode : BaseWorkNode
            The work node to be prepared.

        Returns
        -------
        BaseWorkNode
            The configured work node.

        Raises
        ------
        RuntimeError
            If a node with the same ID already exists in the pipeline.
        """
        if new_worknode.id in self.flow_ids:
            err_msg = f"{new_worknode=} already present. Pipeline can't hold WorkNodes with duplicated ids."
            self.logger.error(err_msg)
            raise RuntimeError(err_msg)
        new_worknode.set_systems(tuple(self.systems.keys()))
        new_worknode.root_dir = self.cwd
        new_worknode.logging_level = self.logging_level
        new_worknode.logging_filemode = "w" if self.new_run else "a"

        return new_worknode

    def _check_edge(self, new_worknode: BaseWorkNode, old_worknode: BaseWorkNode) -> None:
        """
        Validate that an edge can be created between two nodes.

        This method ensures that the nodes being connected are valid and that
        the connection itself is logical (e.g., a node cannot be connected
        to itself).

        Parameters
        ----------
        new_worknode : BaseWorkNode
            The source node of the edge.
        old_worknode : BaseWorkNode
            The destination node of the edge.

        Raises
        ------
        RuntimeError
            If the destination node is not in the flow or if the source and
            destination nodes are the same.
        """
        if old_worknode not in self.flow.nodes:
            err_msg = f"{old_worknode=} not found in the Pipeline's flow. Cannot have disjoint graphs."
            self.logger.error(err_msg)
            raise RuntimeError(err_msg)
        if old_worknode.id == new_worknode.id:
            err_msg = "Cannot append a WorkNode to itself."
            self.logger.error(err_msg)
            raise RuntimeError(err_msg)

    def append_node(
        self, new_worknode: BaseWorkNode, old_worknodes: Collection[BaseWorkNode] = tuple(), update_leafs: bool = True
    ) -> list[BaseWorkNode]:
        """
        Append a new work node to existing nodes in the workflow graph.

        This method adds a new node to the pipeline and connects it to one or
        more existing nodes. If no existing nodes are specified, the new node
        is connected to all current leaf nodes.

        Parameters
        ----------
        new_worknode : BaseWorkNode
            The new node to be added to the graph.
        old_worknodes : Collection[BaseWorkNode], optional
            A sequence of existing nodes to connect the new node to. If empty,
            the new node will be connected to all current leaf nodes.
        update_leafs : bool, optional
            If True, the `old_worknodes` that are also leaf nodes will be removed from the leaf nodes.

        Returns
        -------
        list[BaseWorkNode]
            The new set of leaf nodes in the workflow graph.

        Raises
        ------
        RuntimeError
            If the new work node's ID already exists in the pipeline or if any
            of the specified `old_worknodes` are not in the flow.
        """
        if not self.nodes_are_new([new_worknode]):
            return self.leafs
        # noinspection PyUnreachableCode
        if not isinstance(old_worknodes, Iterable):
            old_worknodes = (old_worknodes,)
            # self.logger.debug(f"`append_node()`: Single `old_worknode` provided: {old_worknodes}.")
        leafs: set[BaseWorkNode] = set(self.leafs) if len(old_worknodes) == 0 else set(old_worknodes)
        new_worknode = self._setup_new_node(new_worknode)
        for node in leafs:
            self._check_edge(new_worknode, node)
            self.flow.add_edge(node, new_worknode)
        self.flow_ids.add(new_worknode.id)
        # Set up the new leaf nodes.
        if update_leafs:
            # Remove those that are connected to the `new_worknode`. They can't be leafs.
            set_leafs = set(self.leafs)
            set_leafs.difference_update(leafs)
            self.leafs = list(set_leafs)
        self.leafs.append(new_worknode)
        return self.leafs

    def nodes_are_new(self, nodes: Iterable[BaseWorkNode]) -> bool:
        common_nodes_ids: set[str] = set(n.id for n in nodes) & set(n.id for n in self.flow.nodes)
        if len(common_nodes_ids) != 0:
            if self.checkpointer.new_run:
                err_msg = (
                    f"WorkNodes already exist in the pipeline: {common_nodes_ids}. "
                    "Pipeline can't hold WorkNodes with duplicated ids."
                )
                self.logger.error(err_msg)
                raise RuntimeError(err_msg)
            else:
                self.logger.debug(
                    f"WorkNodes already exist in the pipeline: {common_nodes_ids}. "
                    "Assuming you want to continue from a checkpoint and doing nothing."
                )
                return False
        return True

    def append_flow(
        self, flow: BaseFlow, old_worknodes: Collection[BaseWorkNode] = tuple(), update_leafs: bool = True
    ) -> list[BaseWorkNode]:
        """
        Append a pre-defined flow (a DAG of work nodes) to the pipeline.

        This method allows for the modular composition of complex workflows by
        appending a pre-defined sequence of work nodes (a `BaseFlow`) to the
        existing workflow graph.

        Parameters
        ----------
        flow : BaseFlow
            The flow instance containing the DAG of work nodes to be appended.
        old_worknodes : Union[BaseWorkNode, list[BaseWorkNode]]
            The existing node or nodes in the graph to connect the new flow to.
        update_leafs : bool
            If True, the `old_worknodes` that are also leaf nodes will be removed from the leaf nodes.

        Returns
        -------
        list[BaseWorkNode]
            A list of the exit nodes from the appended flow, which can be used
            for further chaining.

        Raises
        ------
        RuntimeError
            If any node from the flow already exists in the pipeline or if a
            specified `left_worknode` is not found.
        """

        if not self.nodes_are_new(flow.dag.nodes):
            return self.leafs

        # Init the leaf nodes from the current flow
        # noinspection PyUnreachableCode
        if not isinstance(old_worknodes, Iterable):
            old_worknodes = (old_worknodes,)
        leafs: set[BaseWorkNode] = set(self.leafs) if len(old_worknodes) == 0 else set(old_worknodes)

        # Set up each of the new nodes
        for node in flow.dag.nodes:
            self._setup_new_node(node)
            self.flow_ids.add(node.id)
        # Join the 2 graphs
        new_flow = nx.compose(self.flow, flow.dag)
        # _fuse_flows() may remove the root node from the current flow if it is a dummy node, so keep it for later
        backup_leafs = deepcopy(leafs)
        self._fuse_flows(leafs, flow.root, new_flow)
        for leaf_node in leafs:
            new_flow.add_edge(leaf_node, flow.root)

        self.flow = new_flow
        ########################### TODO ###########################
        ########### Can't we just do away with `old_wornodes` and force append_flow to append the new flow too all the
        ########### leafs and then set the new flow leaf as the whole pipeline leaf?
        # Set up the new leaf nodes.
        if update_leafs:
            # Remove those that are connected to the `new_worknode`. They can't be leafs.
            set_leafs = set(self.leafs)
            set_leafs.difference_update(backup_leafs)
            self.leafs = list(set_leafs)

        self.leafs.append(flow.leaf)
        ########################### ###########################
        return self.leafs

    def _fuse_flows(self, leafs: set[BaseWorkNode], root: BaseWorkNode, new_flow: nx.DiGraph) -> None:
        """
        Add edges between the pipeline leaf nodes and the root node of the incoming flow. If it's just dummy nodes
        on both ends, discard the dummy from the incoming flow.

        Parameters
        ----------
        leafs : set[BaseWorkNode]
            The set of leaf nodes that may or may not be just a dummy node.
        root : BaseWorkNode
            The dummy root node from the incoming flow.
        new_flow : nx.DiGraph
            The new flow to which the edges will be added.
        """
        if len(leafs) == 1:
            leaf_node = leafs.pop()
            if isinstance(leaf_node, WorkNodeDummy):
                self.logger.info(f"Fusing dummy {leaf_node} into {root.id}")
                for successor in new_flow.successors(root):
                    new_flow.add_edge(leaf_node, successor)
                new_flow.remove_node(root)
                return
            else:
                new_flow.add_edge(leaf_node, root)
                return
        for leaf_node in leafs:
            new_flow.add_edge(leaf_node, root)

    def add_edge(self, left_worknode: BaseWorkNode, right_worknode: BaseWorkNode) -> BaseWorkNode:
        """
        Add a directed edge between two existing nodes in the workflow.

        This method allows for the creation of more complex, non-linear
        workflows by adding explicit dependencies between nodes that are
        already part of the graph.

        Parameters
        ----------
        left_worknode : BaseWorkNode
            The source node for the edge.
        right_worknode : BaseWorkNode
            The destination node for the edge.

        Returns
        -------
        BaseWorkNode
            The destination work node.

        Raises
        ------
        RuntimeError
            If either of the nodes is not already in the flow.
        """
        if left_worknode.id in self.flow_ids and right_worknode.id in self.flow_ids:
            self.flow.add_edge(left_worknode, right_worknode)
        else:
            err_msg = (
                f"Both {left_worknode=} and {right_worknode=} have to be present in the Pipeline's flow to add an edge."
                " Use `append_node()` instead to add a new node to the flow."
            )
            self.logger.error(err_msg)
            raise RuntimeError(err_msg)

        if left_worknode.id in self.leafs:
            # If the left_worknode is a leaf, it can't be a leaf anymore.
            self.leafs.remove(left_worknode)
        return right_worknode

    def get_node_map(self) -> dict[str, BaseWorkNode]:
        """
        Create a mapping of work node IDs to their corresponding work node instances.

        Useful for checking what the current flow looks like.

        Returns
        -------
        dict[str, BaseWorkNode]
            A dictionary mapping work node IDs to their instances.
        """
        return {node.id: node for node in self.flow.nodes}

    @staticmethod
    def get_amber_version(logger: logging.Logger) -> None:
        """
        Log the version of the pmemd execution engine.

        This function checks for the AMBERHOME environment variable, which is
        standard in AmberTools installations. It then attempts to get the version
        number by running the pmemd command.

        Parameters
        ----------
        logger : logging.Logger
            The logger to use for logging messages.

        Raises
        ------
        EnvironmentError
            If the AMBERHOME environment variable is not set.
        """
        amber_home = os.environ.get("AMBERHOME")
        if not amber_home:
            logger.warning("The AMBERHOME environment variable is not set. Make sure you know what you're doing.")
        else:
            for engine in ("pmemd ", "pmemd.cuda", "pmemd.cuda.MPI"):
                p = sp.run(f"{engine} --version", stdout=sp.PIPE, stderr=sp.PIPE, text=True, shell=True)
                try:
                    match = re.search(r"\d+\.\d+", p.stdout.strip())
                    version = float(match.group(0))
                    logger.info(f"Found {engine=} with {version=}")
                except (ValueError, AttributeError):
                    logger.warning(f"Could not find a version number for '{engine}'")

    # noinspection PyUnresolvedReferences
    @force_restart.validator
    def _check_ignore_checkpoint(self, _, value):
        """
        Validate that `force_restart` and `ignore_checkpoint` are not both set to True.

        Parameters
        ----------
        _
            The attribute being validated (unused).
        value : bool
            The value of `force_restart`.

        Raises
        ------
        ValueError
            If both `force_restart` and `ignore_checkpoint` are True.
        """
        if value is True and self.ignore_checkpoint is True:
            raise ValueError("Cannot set `force_restart=True` and `ignore_checkpoint=True` simultaneously.")

    @staticmethod
    def clean(checkpoint_path) -> None:
        """
        Remove the checkpoint file.

        Parameters
        ----------
        checkpoint_path : Path
            The path to the checkpoint file to be removed.
        """
        checkpoint_path.unlink()

    # noinspection PyUnresolvedReferences
    @target.validator
    def _prot_or_rdname(self, attribute, value: str):
        """
        Validate that the 'target' attribute is either 'protein' or 'na'.

        Parameters
        ----------
        attribute
            The attribute being validated (unused).
        value : str
            The value of the 'target' attribute.

        Raises
        ------
        RuntimeError
            If the value is not 'protein' or 'na'.
        """
        if value != "protein" and value != "na":
            raise RuntimeError(f"{attribute} must be 'protein' or 'na'")

    def __getstate__(self) -> dict:
        """
        Customize the pickling process for the Pipeline class.

        This method excludes the unpicklable 'logger' attribute from the
        state that is saved during pickling. The rest of the attributes
        are handled automatically by the `attrs` library.

        Returns
        -------
        dict
            A dictionary representing the state of the object to be pickled.
        """
        # Remove the logger and `__weakref__`  from the state to avoid pickling issues
        # noinspection PyUnresolvedReferences
        state = {
            slot: getattr(self, slot) for slot in self.__class__.__slots__ if slot not in ("logger", "__weakref__")
        }
        return state

    def __setstate__(self, state: dict):
        """
        Customize the unpickling process for the Pipeline class.

        This method re-initializes the logger after all other attributes have
        been restored from the pickled state. This ensures that the pipeline
        can continue logging correctly after being unpickled.

        Parameters
        ----------
        state : dict
            A dictionary representing the pickled state of the object.
        """
        # Manually set the attributes from the state dictionary
        for key, value in state.items():
            super().__setattr__(key, value)

        # Re-create the logger instance, ensuring it appends to the existing log file
        self.logger = set_logger(
            Path(self.cwd, f"{self.name}.log"),
            logging_level=self.logging_level,
            filemode="a",  # Always append ('a') to the log file from a pickled instance
        )

    def draw(
        self, *, output_filename: Optional[str] = None, figsize: tuple[int, int] = (18, 18), node_size: int = 700
    ) -> None:
        draw_flow_graph(self.flow, output_filename=output_filename, figsize=figsize, node_size=node_size)


def change_cwd(
    cwd: Path,
    new_cwd: Path,
    systems: dict[str, dirpath_t],
    artifacts: PipelineArtifacts,
    flow: nx.DiGraph,
    checkpointer: Optional[PipelineCheckpointer] = None,
    systems_subset: Optional[Sequence[str]] = None,
) -> tuple[Path, dict[str, Path], PipelineArtifacts, nx.DiGraph]:
    if checkpointer is not None:
        rel_cpt_path = checkpointer.checkpoint_path.relative_to(cwd)
        new_cpt_path = Path(new_cwd, rel_cpt_path)
        checkpointer.checkpoint_path = new_cpt_path

    # If the pipeline is being run remotely, we need to ensure that the all the absolute paths are within the
    # remote base directory.
    if systems_subset is None:
        systems_subset = list(systems.keys())
    systems = {
        sysname: Path(new_cwd, Path(sysdir).relative_to(cwd))
        for sysname, sysdir in systems.items()
        if sysname in systems_subset
    }
    if len(systems) == 0:
        raise ValueError(f"No valid systems found in the provided {systems_subset=}")

    # If we're starting from a checkpoint, we need to ensure that the artifacts are also set to the remote base directory.
    for node_id, batch_artifacts in artifacts.items():
        batch_artifacts.change_base_dir(cwd, new_cwd)
    # Set the current working directory for the local pipeline to the remote base directory
    for node in flow:
        node.root_dir = new_cwd

    return new_cwd, systems, artifacts, flow
