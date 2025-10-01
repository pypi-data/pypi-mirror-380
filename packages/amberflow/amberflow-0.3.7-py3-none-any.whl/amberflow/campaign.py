import logging
import time
from collections import deque
from pathlib import Path
from typing import Sequence, Collection

from amberflow.checkpoint import CampaignCheckpointer
from amberflow.distributed import Batch, BatchStatus, BatchCommand
from amberflow.distributed import split_pipeline
from amberflow.flows import BaseFlow
from amberflow.pipeline import Pipeline
from amberflow.primitives import set_logger, dirpath_t
from amberflow.worknodes import WorkNodeStatus, BaseWorkNode


class Campaign:
    """
    Orchestrates the execution of a Pipeline across multiple systems, batched and distributed across multiple execution
    sites.
    """

    def __init__(
        self,
        name: str,
        pipeline: Pipeline,
        cwd: Path,
        sites: Sequence[BatchCommand],
        systems_per_batch: int,
        logging_level: int = logging.INFO,
        poll_interval_mins: int | float = 5,
        ignore_checkpoint: bool = False,
        force_restart: bool = False,
    ):
        self.name = name
        self._setup_cwd(cwd)
        self.sites = sites
        self.systems_per_batch = systems_per_batch
        self.checkpoint_filename = f"campaign_cpt_{self.name}.pkl"
        self.checkpoint_path = Path(self.cwd, self.checkpoint_filename)

        self.pipeline = pipeline
        self.batches: list[Batch] | None = None

        self.checkpointer = CampaignCheckpointer(
            self.name,
            tracked_obj=self,
            checkpoint_path=self.checkpoint_path,
            ignore_checkpoint=ignore_checkpoint,
            force_restart=force_restart,
        )

        self.logger = set_logger(
            Path(self.cwd, f"{self.name}.log"),
            logging_level=logging_level,
            filemode="w" if self.checkpointer.new_run else "a",
        )
        self.poll_interval_mins = poll_interval_mins

    def _setup_cwd(self, cwd: dirpath_t) -> None:
        self.cwd = Path(cwd)
        if not self.cwd.is_dir():
            err_msg = f"Provided cwd {self.cwd} is not a directory."
            raise NotADirectoryError(err_msg)

    def _setup_checkpoint(self, cwd: dirpath_t, ignore_checkpoint: bool) -> bool:
        self.checkpoint_path = Path(cwd, self.checkpoint_filename)
        # If user sets `ignore_checkpoint` to True, we will always start a new run.
        self.ignore_checkpoint = ignore_checkpoint
        return not self.checkpoint_path.is_file() or self.ignore_checkpoint

    def _setup_batches(self) -> list[Batch]:
        """Splits systems into batches and initializes self.batches."""

        all_systems = sorted(list(self.pipeline.systems.keys()))
        system_chunks: list[set[str]] = [
            set(all_systems[i : i + self.systems_per_batch]) for i in range(0, len(all_systems), self.systems_per_batch)
        ]

        batches = []
        for b, batch_systems in enumerate(system_chunks):
            batch_id = f"batch_{self.name}_{b:04d}"
            # noinspection PyTypeChecker
            new_pipeline = split_pipeline(
                pipeline=self.pipeline,
                batch_systems=batch_systems,
                new_name=batch_id,
            )
            batches.append(
                Batch(
                    id=batch_id,
                    status=BatchStatus.PENDING,
                    systems=batch_systems,
                    pipeline=new_pipeline,
                    state=new_pipeline.checkpointer.get_state(),
                    pickle_filename=new_pipeline.pickle_filename,
                    checkpoint_filename=new_pipeline.checkpointer.name,
                )
            )

            self.logger.info(f"Batch {batch_id}  with systems {batch_systems} initialized.")

        return batches

    def launch_all(self):
        """
        Launches the campaign by managing a queue of batches, dispatching them to available command slots,
        and polling for their completion.
        """
        self.batches: list[Batch] = self._setup_batches()

        available_sites: list[BatchCommand] = list(self.sites)
        remaining_batches = deque(self.batches)
        if not self.checkpointer.new_run:
            remaining_batches = self._find_done_jobs(available_sites, remaining_batches)
        self.logger.info(f"Starting campaign launch with {len(remaining_batches)} batches.")
        status_batches: dict[str, BatchStatus] = {b.id: b.status for b in self.batches}
        running_jobs: dict[str, BatchCommand] = {}

        while remaining_batches or len(running_jobs) != 0:
            # Now we know that all `remaining_batches` are not yet completed. There may be some actual running jobs.
            new_jobs = self._attach_to_available(available_sites, remaining_batches)
            self._launch_available(new_jobs, status_batches)
            running_jobs.update(new_jobs)

            self.logger.info(
                f"{len(running_jobs)} jobs running, {len(remaining_batches)} jobs in queue. "
                f"Waiting for {self.poll_interval_mins} minutes"
            )
            self.checkpointer.save(self.logger)
            time.sleep(self.poll_interval_mins * 60)
            done_batch_ids = self._sync_jobs(running_jobs)
            freed_up_sites = self._clean_done_jobs(done_batch_ids, running_jobs)
            available_sites.extend(freed_up_sites)

        done_all_nodes = all([batch.status == BatchStatus.COMPLETED for batch in self.batches])
        if done_all_nodes:
            for node in self.pipeline.flow.nodes:
                node.status = WorkNodeStatus.COMPLETED

        self.logger.info("Campaign has completed all batches.")

    def _sync_jobs(self, running_jobs: dict[str, BatchCommand]) -> list[str]:
        done_jobs = []
        for batch_id, batch_command in running_jobs.items():
            if batch_command.sync_batch(self.logger):
                done_jobs.append(batch_id)
            self.sync_pipelines(self.pipeline, batch_command.batch.pipeline)
        return done_jobs

    def _clean_done_jobs(self, done_jobs: list[str], running_jobs: dict[str, BatchCommand]) -> list[BatchCommand]:
        """Tries to clean up finished jobs from running_jobs and returns True if successful.
        If no jobs are done, returns False."""

        available_sites: list[BatchCommand] = []
        if len(done_jobs) > 0:
            for batch_id in done_jobs:
                try:
                    available_sites.append(running_jobs.pop(batch_id))
                    self.logger.info(f"Batch {batch_id} has finished.")
                except KeyError:
                    self.logger.warning(f"Batch {batch_id} was not found in running jobs. This should not happen.")
        return available_sites

    def _launch_available(self, running_jobs: dict[str, BatchCommand], status_batches: dict[str, BatchStatus]) -> None:
        for batch_id, batch_command in running_jobs.items():
            if status_batches[batch_id] != BatchStatus.RUNNING:
                batch_command.run(self.logger)
                status_batches[batch_id] = BatchStatus.RUNNING

    def _attach_to_available(
        self, available_sites: list[BatchCommand], remaining_batches: deque[Batch]
    ) -> dict[str, BatchCommand]:
        running_jobs: dict[str, BatchCommand] = {}
        while available_sites and remaining_batches:
            batch_command = available_sites.pop(0)
            batch = remaining_batches.popleft()
            try:
                batch_command.attach_batch(batch, self.logger)
                running_jobs[batch.id] = batch_command
            except Exception as e:
                self.logger.error(f"Failed to launch batch {batch.id}: {e}", exc_info=True)
                batch.status = BatchStatus.FAILED
        return running_jobs

    def _find_done_jobs(self, sites: list[BatchCommand], batches: deque[Batch]) -> deque[Batch]:
        """
        TODO: what if it finds a checkpoint with different systems? The user should split the campaigns
        """
        n_batches = len(batches)
        for _ in range(n_batches):
            batch = batches.popleft()
            is_done = False
            for site_cmd in sites:
                site_cmd.attach_batch(batch, self.logger)
                if site_cmd.sync_batch(self.logger):
                    self.sync_pipelines(self.pipeline, site_cmd.batch.pipeline)
                    is_done = True
                    break
            if not is_done:
                batches.append(batch)
        return batches

    def append_flow(
        self, flow: BaseFlow, old_worknodes: Collection[BaseWorkNode] = tuple(), update_leafs: bool = True
    ) -> list[BaseWorkNode]:
        return self.pipeline.append_flow(flow, old_worknodes=old_worknodes, update_leafs=update_leafs)

    def append_node(
        self, new_worknode: BaseWorkNode, old_worknodes: Collection[BaseWorkNode] = tuple(), update_leafs: bool = True
    ) -> list[BaseWorkNode]:
        return self.pipeline.append_node(new_worknode, old_worknodes=old_worknodes, update_leafs=update_leafs)

    def get_node_map(self) -> dict[str, BaseWorkNode]:
        return self.pipeline.get_node_map()

    @staticmethod
    def sync_pipelines(destination_pipeline: Pipeline, source_pipeline: Pipeline) -> None:
        state = source_pipeline.checkpointer.get_state()
        destination_pipeline.sync_state_if_newer(state)
