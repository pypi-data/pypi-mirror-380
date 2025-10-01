import shutil
import warnings
from pathlib import Path
from typing import Any, Literal

import MDAnalysis as mda
import parmed

# noinspection PyUnresolvedReferences,PyProtectedMember
from parmed.tools import addPDB

from amberflow.artifacts import (
    BaseArtifact,
    ArtifactContainer,
    BaseStructureFile,
    BaseTopologyFile,
    ArtifactRegistry,
    BinderLigandPDB,
    BaseFrcmodFile,
    BaseLibFile,
)
from amberflow.primitives import dirpath_t, filepath_t, remove_residues_pdb, patch_pdb_lib
from amberflow.worknodes import BaseSingleWorkNode, worknodehelper

__all__ = ("Ambpdb", "PatchPDBLib")


@worknodehelper(
    file_exists=True,
    input_artifact_types=(BaseStructureFile, BaseTopologyFile),
    output_artifact_types=(BaseArtifact,),
)
class Ambpdb(BaseSingleWorkNode):
    SOLVENT_SELECTION = {
        "parmed": ":WAT,:HOH,:Na+,:Cl-,:NA,:CL",
        "mdanalysis": "not (resname WAT or resname HOH or resname Na+ or resname Cl- or resname NA or resname CL)",
        "ambpdb": ("WAT", "Cl-", "CL", "Na+", "NA"),
    }

    def __init__(
        self,
        wnid: str,
        *args,
        method: Literal["mdanalysis", "ambpdb", "parmed"] = "ambpdb",
        strip_solvent: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(
            wnid=wnid,
            *args,
            **kwargs,
        )
        self.strip_solvent = strip_solvent
        self.method = method

    def _run(
        self,
        *,
        cwd: dirpath_t,
        sysname: str,
        **kwargs,
    ) -> Any:
        in_top = Path(self.input_artifacts["BaseTopologyFile"])
        # template: Optional[Path] = None
        if template := self.input_artifacts.get("BaseDockComplexStructureFile"):
            template = Path(template)
            new_artifacts = ArtifactContainer.from_other(self.input_artifacts, "BaseDockComplexStructureFile")
        else:
            new_artifacts = self.input_artifacts
        in_rst7 = Path(new_artifacts["BaseStructureFile"])
        out_pdb = self.work_dir / f"{in_rst7.stem}.pdb"

        if self.skippable:
            if self._try_and_skip(sysname, out_pdb=out_pdb):
                return self.output_artifacts

        if self.method == "mdanalysis":
            self.mdanalysis(in_top, in_rst7, out_pdb)
        elif self.method == "ambpdb":
            self.ambpdb(in_top, in_rst7, out_pdb)
        elif self.method == "parmed":
            mol = parmed.load_file(str(in_top), str(in_rst7))
            # if template := new_artifacts["BaseDockComplexStructureFile"]:
            if template is not None:
                addPDB(mol, str(template)).execute()
            if self.strip_solvent:
                strip_selection = parmed.amber.AmberMask(mol, self.SOLVENT_SELECTION["parmed"])
                # noinspection PyUnresolvedReferences
                atoms_to_strip = ";".join([f"{mol[idx].number} {mol[idx].name}" for idx in strip_selection.Selected()])
                self.node_logger.info(f"Will strip the following atoms:\n{atoms_to_strip}")
                # noinspection PyUnresolvedReferences
                mol.strip(self.SOLVENT_SELECTION["parmed"])
            self.node_logger.info(f"Writing {out_pdb}")
            # noinspection PyUnresolvedReferences
            mol.save(str(out_pdb), overwrite=True)

        self.output_artifacts = self.fill_output_artifacts(sysname, out_pdb=out_pdb)
        return self.output_artifacts

    def mdanalysis(self, in_top: filepath_t, in_rst7: filepath_t, out_pdb: filepath_t):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            u = mda.Universe(str(in_top), str(in_rst7))
        if self.strip_solvent:
            self.node_logger.info(f"Stripping atoms with mask: {self.SOLVENT_SELECTION['parmed']}")
            strip_selection = u.select_atoms(self.SOLVENT_SELECTION["parmed"])
            atoms_to_strip = ";".join([f"{atom.index} {atom.name}" for atom in strip_selection])
            self.node_logger.info(f"Will strip the following soft-core atoms from target ligand:\n{atoms_to_strip}")
            strip_selection.remove()
        self.node_logger.info(f"Writing {out_pdb}")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            u.atoms.write(str(out_pdb))

    def ambpdb(self, in_top: filepath_t, in_rst7: filepath_t, out_pdb: filepath_t):
        self.command.run(
            ["ambpdb", "-p", str(in_top), "-c", str(in_rst7), ">", str(out_pdb)],
            cwd=self.work_dir,
            logger=self.node_logger,
            expected=(out_pdb,),
        )
        # noinspection PyTypeChecker
        resnames: tuple[str] = self.SOLVENT_SELECTION[self.method]
        remove_residues_pdb(out_pdb, out_pdb, resnames)

    # noinspection DuplicatedCode
    def _try_and_skip(self, sysname: str, *, out_pdb: filepath_t) -> bool:
        if self.skippable:
            try:
                self.output_artifacts = self.fill_output_artifacts(sysname, out_pdb=out_pdb)
                self.node_logger.info(f"Skipped {self.id} WorkNode.")
                return True
            except (FileNotFoundError, ValueError) as e:
                self.node_logger.debug(f"Can't skip {self.id} Got: {e}")
            except NotImplementedError:
                self.node_logger.debug(
                    f"Can't skip {self.id}. {self.__class__.__name__} did not implement `fill_output_artifacts()`"
                )
        return False

    def fill_output_artifacts(self, sysname: str, *, out_pdb: filepath_t) -> ArtifactContainer:
        tags = self.tags[self.artifact_map["BaseStructureFile"]]
        return ArtifactContainer(sysname, [ArtifactRegistry.create_instance_by_filename(out_pdb, tags=tags)])


@worknodehelper(
    file_exists=True,
    input_artifact_types=(BinderLigandPDB, BaseLibFile),
    output_artifact_types=(BinderLigandPDB, BaseLibFile, BaseFrcmodFile),
    optional_artifact_types=(BaseFrcmodFile,),
)
class PatchPDBLib(BaseSingleWorkNode):
    def __init__(
        self,
        wnid: str,
        *args,
        patch_lib_coords: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(
            wnid=wnid,
            *args,
            **kwargs,
        )
        self.patch_lib_coords = patch_lib_coords

    def _run(
        self,
        *,
        cwd: dirpath_t,
        sysname: str,
        **kwargs,
    ) -> Any:
        in_lib = Path(self.input_artifacts["BaseLibFile"])
        in_pdb = Path(self.input_artifacts["BinderLigandPDB"])
        self.node_logger.info(f"Patching {in_lib} using {in_pdb}")
        out_pdb = self.work_dir / in_pdb.name
        out_lib = self.work_dir / in_lib.name
        patch_pdb_lib(in_pdb, in_lib, out_pdb, out_lib, logger=self.node_logger)
        self.output_artifacts = self.fill_output_artifacts(sysname, out_pdb=out_pdb, out_lib=out_lib)
        return self.output_artifacts

    # noinspection DuplicatedCode
    def _try_and_skip(self, sysname: str, *, out_pdb: filepath_t, out_lib: filepath_t) -> bool:
        if self.skippable:
            try:
                self.output_artifacts = self.fill_output_artifacts(sysname, out_pdb=out_pdb, out_lib=out_lib)
                self.node_logger.info(f"Skipped {self.id} WorkNode.")
                return True
            except (FileNotFoundError, ValueError) as e:
                self.node_logger.debug(f"Can't skip {self.id} Got: {e}")
            except NotImplementedError:
                self.node_logger.debug(
                    f"Can't skip {self.id}. {self.__class__.__name__} did not implement `fill_output_artifacts()`"
                )
        return False

    def fill_output_artifacts(self, sysname: str, *, out_pdb: filepath_t, out_lib: filepath_t) -> ArtifactContainer:
        artifacts = [
            ArtifactRegistry.create_instance_by_filename(out_pdb),
            ArtifactRegistry.create_instance_by_filename(out_lib),
        ]
        try:
            in_frcmod = Path(self.input_artifacts["BaseFrcmodFile"])
            out_frcmod = self.work_dir / in_frcmod.name
            shutil.copy(in_frcmod, out_frcmod)
            artifacts.append(ArtifactRegistry.create_instance_by_filename(out_frcmod))
        except KeyError:
            self.node_logger.info("No input frcmod provided, skipping copying it to output artifacts.")
        return ArtifactContainer(sysname, artifacts)
