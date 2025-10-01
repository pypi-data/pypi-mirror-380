"""
Provides a collection of utility and helper worknodes for data workflows.

This module contains a variety of `WorkNode` implementations that perform common,
reusable tasks within a larger data processing pipeline. These nodes handle
operations such as filtering artifacts, merging structural data, collecting
files, and performing specialized file modifications like adding chain IDs to
PDB files.

Classes
-------
WorkNodeDummy
    A simple node that copies its input artifacts to its output.
Filter
    Selectively passes through artifacts based on their type.
JoinTargetBinder
    Merges protein (target) and ligand (binder) structure files into a
    single complex.
CollectFiles
    A base class for nodes that gather and potentially link files.
AddChainid
    Assigns unique, sequential chain IDs to molecules within a PDB file.
"""

import os
import string
import warnings
from pathlib import Path
from typing import Optional, Sequence, List, Type

import MDAnalysis as mda
import numpy as np
from typing_extensions import override

from amberflow.artifacts import (
    BaseArtifact,
    ArtifactContainer,
    BaseTargetStructureFile,
    BinderLigandPDB,
    BaseBinderStructureFile,
    ArtifactRegistry,
    BaseStructureFile,
)
from amberflow.primitives import dirpath_t, WorkNodeRunningError, assign_chain_ids
from amberflow.worknodes import worknodehelper, BaseSingleWorkNode, runiverse, wuniverse

__all__ = [
    "WorkNodeDummy",
    "Filter",
    "JoinTargetBinder",
    "CollectFiles",
    "AddChainid",
    "ImpossibleFilter",
]


@worknodehelper(file_exists=True, input_artifact_types=(BaseArtifact,))
class WorkNodeDummy(BaseSingleWorkNode):
    """
    A simple worknode that copies all input artifacts to its output.

    This node serves as a placeholder or a simple pass-through mechanism in a
    workflow, duplicating its inputs without modification. It's useful for
    debugging or forking workflow paths.
    """

    @override
    def __init__(
        self,
        wnid: str,
        *args,
        **kwargs,
    ):
        """
        Initializes the WorkNodeDummy instance.

        Args:
            wnid (str): A unique identifier for the worknode instance.
            *args: Positional arguments passed to the parent class.
            **kwargs: Keyword arguments passed to the parent class.
        """
        super().__init__(wnid=wnid, *args, **kwargs)

    @override
    def _run(
        self,
        *args,
        cwd: dirpath_t,
        sysname: str,
        **kwargs,
    ) -> ArtifactContainer:
        # This is all that the dummy node does:
        output_artifacts = []
        for arts in self.input_artifacts.values():
            for artifact in arts:
                try:
                    copy_to_method = getattr(artifact, "copy_to")
                    output_artifacts.append(copy_to_method(self.work_dir))
                except AttributeError:
                    self.node_logger.warning(
                        f"Artifact {artifact} of class {artifact.__class__.__name__} does not have a copy_to() method."
                    )
        self.output_artifacts = ArtifactContainer(sysname, output_artifacts)
        return self.output_artifacts

    def __repr__(self) -> str:
        return f"WorkNodeDummy(id={self.id})"


@worknodehelper(file_exists=True)
class Filter(BaseSingleWorkNode):
    """
    A worknode that filters artifacts based on their type.

    This node can be configured to either include or exclude a specified list
    of artifact types, allowing for selective processing in a workflow.
    """

    @override
    def __init__(
        self,
        wnid: str,
        *args,
        artifact_types: Sequence[Type],
        in_or_out: str = "in",
        fail_if_no_artifacts: bool = False,
        single: bool = False,
        **kwargs,
    ):
        """
        Initializes the Filter instance.

        Args:
            wnid (str): A unique identifier for the worknode instance.
            artifact_types (Sequence[type]): A sequence of artifact classes to
                be used for filtering.
            in_or_out (str): Determines the filtering logic. "in" to keep
                matching types, "out" to keep non-matching types.
            *args: Positional arguments passed to the parent class.
            **kwargs: Keyword arguments passed to the parent class.
        """
        super().__init__(wnid=wnid, *args, **kwargs)
        self.artifact_types = tuple(artifact_types)
        if in_or_out not in ("in", "out"):
            raise ValueError(f"in_or_out must be 'in' or 'out', got {in_or_out}.")
        self.in_or_out = in_or_out
        self.fail_if_no_artifacts = fail_if_no_artifacts
        self.single = single

    def _run(
        self,
        *args,
        cwd: dirpath_t,
        sysname: str,
        **kwargs,
    ) -> ArtifactContainer:
        """
        Executes the filtering logic on the input artifacts.

        Args:
            cwd (dirpath_t): The working directory for this execution.
            sysname (str): The name of the system being processed.
            **kwargs: Additional keyword arguments.

        Returns:
            An ArtifactContainer holding the artifacts that passed the filter.
        """
        output_artifacts: List[BaseArtifact] = []
        for arts in self.input_artifacts.values():
            for artifact in arts:
                is_instance = isinstance(artifact, self.artifact_types)
                if (is_instance and self.in_or_out == "in") or (not is_instance and self.in_or_out == "out"):
                    self._add(artifact, output_artifacts)

        no_artifacts = len(output_artifacts) == 0
        if no_artifacts:
            art_types_str = ", ".join([art_type.__name__ for art_type in self.artifact_types])
            err_msg = f"No artifacts passed the filter with types {art_types_str} and mode '{self.in_or_out}'."
            if self.fail_if_no_artifacts:
                self.node_logger.warning(err_msg)
                raise WorkNodeRunningError(err_msg)
            else:
                self.node_logger.warning(err_msg)

        if self.single:
            all_types = [type(artifact) for artifact in output_artifacts]
            if len(set(all_types)) < len(all_types):
                err_msg = f"Filter node {self.id} set to single=True but multiple artifacts of the same type were found: {all_types}"
                self.node_logger.error(err_msg)
                raise WorkNodeRunningError(err_msg)

        self.output_artifacts = ArtifactContainer(sysname, output_artifacts)
        return self.output_artifacts

    def _add(self, artifact: BaseArtifact, output_artifacts: list[BaseArtifact]) -> None:
        """
        Copies the artifact to the work directory and adds it to the output list.
        """
        if hasattr(artifact, "filepath"):
            copy_to_method = getattr(artifact, "copy_to")
            output_artifacts.append(copy_to_method(self.work_dir))
        else:
            output_artifacts.append(artifact)

    def _try_and_skip(self, sysname: str) -> bool:
        raise NotImplementedError

    def fill_output_artifacts(
        self,
        sysname: str,
    ) -> ArtifactContainer:
        raise NotImplementedError

    def __repr__(self) -> str:
        """Provides a developer-friendly representation of the node."""
        return f"{self.__class__.__name__}(id={self.id}, artifact_types={self.artifact_types})"


@worknodehelper(file_exists=True, input_artifact_types=(BaseTargetStructureFile, BinderLigandPDB))
class JoinTargetBinder(BaseSingleWorkNode):
    """
    Merges separate target (e.g., protein) and binder (e.g., ligand)
    structure files into a single complex structure file (PDB).
    """

    @override
    def __init__(
        self,
        wnid: str,
        *args,
        binder_first: bool = True,
        to_guess: Optional[tuple] = None,
        renumber: bool = False,
        starting_residue: int = 1,
        **kwargs,
    ):
        """
        Initializes the JoinTargetBinder instance.

        Args:
            wnid (str): A unique identifier for the worknode instance.
            binder_first (bool): If True, the binder's atoms will appear first
                in the output file. Otherwise, the target's atoms will.
            to_guess (Optional[tuple]): Options passed to MDAnalysis for guessing
                bond information when reading structures.
            renumber (bool): If True, renumbers residues sequentially starting
                from `starting_residue`.
            starting_residue (int): The starting number for residue renumbering.
            *args: Positional arguments passed to the parent class.
            **kwargs: Keyword arguments passed to the parent class.
        """
        super().__init__(wnid=wnid, *args, **kwargs)
        self.binder_first = binder_first
        self.renumber = renumber
        self.starting_residue = starting_residue
        self.to_guess = to_guess

    def _run(
        self,
        *args,
        cwd: dirpath_t,
        sysname: str,
        **kwargs,
    ) -> ArtifactContainer:
        """
        Executes the merging logic.

        Args:
            cwd (dirpath_t): The working directory for this execution.
            sysname (str): The name of the system being processed.
            **kwargs: Additional keyword arguments.

        Returns:
            An ArtifactContainer with the newly created complex structure file.

        Raises:
            AttributeError: If an unexpected artifact type is encountered.
        """
        utarget: Optional[mda.Universe] = None
        ubinder: Optional[mda.Universe] = None
        for arts in self.input_artifacts.values():
            for artifact in arts:
                if isinstance(artifact, BaseTargetStructureFile):
                    self.node_logger.debug(f"Found target structure file: {artifact}")
                    utarget = runiverse(artifact, to_guess=self.to_guess)
                elif isinstance(artifact, BaseBinderStructureFile):
                    self.node_logger.debug(f"Found binder structure file: {artifact}")
                    ubinder = runiverse(artifact, to_guess=self.to_guess)
                else:
                    err_msg = f"Artifact {artifact} is not a BaseTargetFile or BaseBinderFile."
                    self.node_logger.error(err_msg)
                    raise AttributeError(err_msg)

        # MDAnalysis doesn't add TER records between segments, thankfully tleap can split molecules based on different
        # chainIDs / segids
        self.fix_chainids(utarget, string.ascii_uppercase, "TAR")
        self.fix_chainids(ubinder, string.ascii_uppercase[-3:], "BIN")

        if not hasattr(ubinder.atoms, "chainIDs") or any(np.equal(ubinder.atoms.chainIDs, "")):
            self.node_logger.warning(
                f"At least 1 atom in {ubinder.filename} lacks a chainID. This may cause issues later."
            )

        if self.binder_first:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                ucpx = mda.Merge(ubinder.atoms, utarget.atoms)
        else:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                ucpx = mda.Merge(utarget.atoms, ubinder.atoms)

        if self.renumber:
            ucpx.residues.resids = np.arange(self.starting_residue, len(ucpx.residues.resids) + self.starting_residue)

        out_pdb = self.work_dir / f"complex_{sysname}.pdb"
        wuniverse(ucpx, out_pdb)

        # TODO: document how to use tags and probably improve the API
        tar_type: str = self.artifact_map["BaseTargetStructureFile"]
        bin_type: str = self.artifact_map["BinderLigandPDB"]
        file_artifact = ArtifactRegistry.create_instance_by_filename(
            out_pdb, tags=self.tags[tar_type] + self.tags[bin_type]
        )

        self.output_artifacts = ArtifactContainer(sysname, (file_artifact,))
        return self.output_artifacts

    def fix_chainids(self, universe: mda.Universe, available_chainids: Sequence[str], segid: str) -> None:
        if not hasattr(universe.atoms, "chainIDs"):
            universe.add_TopologyAttr("chainID")
            self.node_logger.warning(f"{universe.filename} lacks chainID information. This may cause issues later.")
        elif any(np.equal(universe.atoms.chainIDs, "")):
            self.node_logger.warning(
                f"At least 1 atom in {universe.filename} lacks a chainID. This may cause issues later."
            )

            for sgmnt, chainid in zip(universe.segments, available_chainids):
                sgmnt.atoms.chainIDs = chainid

        # Assign a unique segid to the binder and another one to the target
        universe.segments.segids = segid

    def _try_and_skip(self, sysname: str) -> bool:
        raise NotImplementedError

    def fill_output_artifacts(
        self,
        sysname: str,
    ) -> ArtifactContainer:
        raise NotImplementedError


@worknodehelper(file_exists=True, input_artifact_types=(BaseArtifact,))
class CollectFiles(BaseSingleWorkNode):
    """
    NOT BEING USED.

    This class is intended to be subclassed. The `symlink_dat_dirs` method
    provides utility for linking directories into the working directory.
    """

    @override
    def __init__(
        self,
        wnid: str,
        *args,
        **kwargs,
    ):
        """
        Initializes the CollectFiles instance.

        Args:
            wnid (str): A unique identifier for the worknode instance.
            *args: Positional arguments passed to the parent class.
            **kwargs: Keyword arguments passed to the parent class.
        """
        super().__init__(wnid=wnid, *args, **kwargs)

    def _run(
        self,
        *args,
        cwd: dirpath_t,
        sysname: str,
        **kwargs,
    ) -> ArtifactContainer:
        """This method must be implemented by subclasses."""
        raise NotImplementedError

    def symlink_dat_dirs(self, dir_list: list[BaseArtifact]) -> Optional[str]:
        """
        Symlinks directory artifacts into the node's working directory.

        It also determines the common 'environment' from the
        artifacts if one exists.

        Args:
            dir_list (list[BaseArtifact]): A list of artifacts that represent
                directories to be linked.

        Returns:
            The common environment string if one is found, otherwise None.

        Raises:
            ValueError: If multiple different environments are detected.
        """
        environment: Optional[str] = None
        if dir_list:
            all_environments = set()
            for datdir in dir_list:
                dirpath = getattr(datdir, "filepath")
                if dirpath is None or not dirpath.is_dir():
                    self.node_logger.warning(f"Artifact {datdir} does not have a valid directory path, skipping.")
                    continue
                parent_filepath = getattr(datdir, "parent_filepath")
                dat_dir_layout = Path(dirpath).relative_to(dirpath).parts
                for i in range(1, len(dat_dir_layout) + 1):
                    current_dat_dirname = Path(*dat_dir_layout[0:i])
                    local_dat_dir = Path(parent_filepath, current_dat_dirname)
                    try:
                        os.symlink(local_dat_dir, self.work_dir / current_dat_dirname, target_is_directory=True)
                    except FileExistsError:
                        continue
                environment = getattr(datdir, "environment")
                all_environments.add(environment)
            if len(all_environments) == 1:
                environment = all_environments.pop()
            elif len(all_environments) > 1:
                raise ValueError(f"Too many environments: {all_environments}. It should be just 1")
        return environment

    def _try_and_skip(self, sysname: str) -> bool:
        raise NotImplementedError

    def fill_output_artifacts(
        self,
        sysname: str,
    ) -> ArtifactContainer:
        raise NotImplementedError


@worknodehelper(file_exists=True, input_artifact_types=(BaseStructureFile,))
class AddChainid(BaseSingleWorkNode):
    """
    A worknode that assigns sequential chain IDs to molecules in a PDB file.

    It identifies separate molecules by 'TER' records and assigns chain IDs
    from A-Z, then a-z. The process is memory-efficient, using memory-mapping
    to modify a copy of the file in place.
    """

    @override
    def __init__(
        self,
        wnid: str,
        *args,
        **kwargs,
    ):
        """
        Initializes the AddChainid instance.

        Args:
            wnid (str): A unique identifier for the worknode instance.
            *args: Positional arguments passed to the parent class.
            **kwargs: Keyword arguments passed to the parent class.
        """
        super().__init__(wnid=wnid, *args, **kwargs)

    def _run(
        self,
        *args,
        cwd: dirpath_t,
        sysname: str,
        **kwargs,
    ) -> ArtifactContainer:
        """
        Executes the chain ID assignment for each input PDB file.

        Args:
            cwd (dirpath_t): The working directory for this execution.
            sysname (str): The name of the system being processed.
            **kwargs: Additional keyword arguments.

        Returns:
            An ArtifactContainer with the modified PDB file artifacts.
        """
        if self._try_and_skip(sysname):
            return self.output_artifacts

        for artifacts in self.input_artifacts.values():
            for art in artifacts:
                if art.filepath.suffix.lower() != ".pdb":
                    self.node_logger.warning(f"{art} is not a PDB file, skipping.")
                    continue
                assign_chain_ids(art.filepath, Path(self.work_dir, art.filepath.name))

        self.output_artifacts = self.fill_output_artifacts(sysname)
        return self.output_artifacts

    def _try_and_skip(self, sysname: str) -> bool:
        """Checks if the node's execution can be skipped."""
        if self.skippable:
            try:
                self.output_artifacts = self.fill_output_artifacts(sysname)
                self.node_logger.info(f"Skipped {self.id} WorkNode.")
                return True
            except (FileNotFoundError, ValueError) as e:
                self.node_logger.info(f"Can't skip {self.id} Got: {e}")
        return False

    def fill_output_artifacts(self, sysname: str) -> ArtifactContainer:
        """Creates output artifacts corresponding to pre-existing files."""
        output_artifacts = [
            ArtifactRegistry.create_instance_by_name(art.__class__.__name__, self.work_dir / art.filepath.name)
            for artifacts in self.input_artifacts.values()
            for art in artifacts
        ]
        return ArtifactContainer(sysname, output_artifacts)


@worknodehelper(file_exists=True)
class ImpossibleFilter(Filter):
    """
    A filtar that blocks all artifacts.

    Used to express a pure job dependency (no data dependency) between 2 nodes on the workflow graph.
    """

    # noinspection PyUnusedLocal
    @override
    def __init__(
        self,
        wnid: str,
        *args,
        **kwargs,
    ):
        super().__init__(wnid=wnid, artifact_types=[BaseArtifact], in_or_out="out")
