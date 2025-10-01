import mmap
import re
import sys
import warnings
from pathlib import Path
from typing import Optional

import MDAnalysis as mda
import parmed

from amberflow.artifacts import (
    BaseMdoutMD,
    BaseComplexTopologyFile,
    ArtifactContainer,
    ArtifactRegistry,
)
from amberflow.artifacts.structure import BaseComplexStructureFile
from amberflow.primitives import (
    filepath_t,
    dirpath_t,
    WorkNodeRunningError,
)
from amberflow.worknodes import (
    worknodehelper,
    BaseFunnelWorkNode,
)

__all__ = ("ProcessTimsDocked",)


@worknodehelper(
    file_exists=True,
    input_artifact_types=(BaseComplexStructureFile, BaseComplexTopologyFile, BaseMdoutMD),
    output_artifact_types=(BaseComplexStructureFile, BaseComplexTopologyFile),
)
class ProcessTimsDocked(BaseFunnelWorkNode):
    """ """

    RESNAME_LIG: dict[str, str] = {"reference": "L00", "target": "L01"}
    MASK_LIG: dict[str, str] = {"reference": ":1", "target": ":2"}
    FINAL_RESNAME: str = "LIG"
    # noinspection RegExpRedundantEscape
    RESTRAINT_PATTERN = re.compile(rb"RESTRAINT\s+=\s+([0-9\.\-]+)")
    FINAL_RESULTS_MARKER = b"FINAL RESULTS"
    SOLUTE_SELECTION = "not (resname WAT or resname HOH or name Na+ Cl- NA CL)"

    def __init__(
        self,
        wnid: str,
        *args,
        get_pdbs: bool = True,
        strip_solvent: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(
            wnid=wnid,
            *args,
            **kwargs,
        )
        self.get_pdbs = get_pdbs
        self.strip_solvent = strip_solvent

    def _run(
        self,
        *,
        cwd: dirpath_t,
        sysname: str,
        binpath: Optional[filepath_t] = None,
        **kwargs,
    ) -> ArtifactContainer:
        final_restraints = {}
        min_restr = float(sys.maxsize)
        best_config = None
        for node_id, art_container in self.input_artifacts.items():
            mdout = Path(art_container["BaseMdoutMD"])
            restraint = self.parse_final_restraint(mdout)
            final_restraints[node_id] = restraint
            if restraint < min_restr:
                min_restr = restraint
                best_config = node_id
                best_top = Path(art_container["BaseComplexTopologyFile"])
                best_rst7 = Path(art_container["BaseComplexStructureFile"])

            self.node_logger.info(f"Final restraint for {node_id}: {restraint}")
            if self.get_pdbs:
                in_top = Path(art_container["BaseComplexTopologyFile"])
                in_rst7 = Path(art_container["BaseComplexStructureFile"])
                out_pdb = self.work_dir / f"{node_id}_{in_top.stem}.pdb"
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    u = mda.Universe(in_top, in_rst7, format="RESTRT")
                    if self.strip_solvent:
                        self.node_logger.info(f"Stripping solvent and ions with selection: {self.SOLUTE_SELECTION}")
                        atomos = u.select_atoms(self.SOLUTE_SELECTION)
                    else:
                        atomos = u.atoms
                    self.node_logger.info(f"Writing {out_pdb}")

                    warnings.simplefilter("ignore")
                    atomos.write(str(out_pdb))
        if best_config is None:
            err_msg = f"Error: Could not determine best configuration for system {sysname}."
            self.node_logger.error(err_msg)
            raise WorkNodeRunningError(err_msg)

        self.node_logger.info(f"Best trial: {best_config} with final restraint {min_restr}")

        # noinspection PyUnboundLocalVariable
        mol = parmed.load_file(str(best_top), str(best_rst7))
        # Set the proper ligand name for the ABFEs:
        # noinspection PyUnresolvedReferences
        mol.residues[1].name = self.FINAL_RESNAME

        strip_selection = parmed.amber.AmberMask(mol, self.MASK_LIG["reference"])
        # noinspection PyUnresolvedReferences
        atoms_to_strip = ";".join([f"{mol[idx].number} {mol[idx].name}" for idx in strip_selection.Selected()])
        self.node_logger.info(f"Will strip the following atoms:\n{atoms_to_strip}")
        # noinspection PyUnresolvedReferences
        mol.strip(self.MASK_LIG["reference"])

        # noinspection PyUnboundLocalVariable
        out_top = self.work_dir / in_top.name
        # noinspection PyUnboundLocalVariable
        out_rst7 = self.work_dir / in_rst7.name
        # noinspection PyUnresolvedReferences
        mol.save(str(out_top), overwrite=True)
        # noinspection PyUnresolvedReferences
        mol.save(str(out_rst7), overwrite=True)

        self.output_artifacts = self.fill_output_artifacts(sysname, out_top=out_top, out_rst7=out_rst7)
        return self.output_artifacts

    def parse_final_restraint(self, in_mdout: filepath_t) -> float:
        """
        Finds the final 'RESTRAINT' value in a file by searching backwards from the end.

        Args:
            in_mdout: input mdout

        Returns:
            The float value of 'RESTRAINT'

        Raises:

        """
        try:
            with open(in_mdout, "rb") as f:
                with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    # Find the start of the "FINAL RESULTS" section, searching backwards
                    final_results_pos = mm.rfind(self.FINAL_RESULTS_MARKER)
                    if final_results_pos == -1:
                        raise ValueError("FINAL RESULTS marker not found in file")

                    # Search for the RESTRAINT pattern from the marker to the end of the file
                    match = self.RESTRAINT_PATTERN.search(mm, final_results_pos)
                    if match:
                        # Extract the captured group, decode from bytes, and cast to float
                        return float(match.group(1).decode())
                    else:
                        raise ValueError("RESTRAINT pattern not found in file")
        except ValueError:
            err_msg = f"Error: Could not convert matched RESTRAINT value to float from file {in_mdout}"
            self.node_logger.error(err_msg)
            raise WorkNodeRunningError(err_msg)

    def _try_and_skip(self, sysname: str) -> bool:
        raise NotImplementedError

    def fill_output_artifacts(
        self,
        sysname: str,
        *,
        out_top: filepath_t,
        out_rst7: filepath_t,
    ) -> ArtifactContainer:
        art_top = ArtifactRegistry.create_instance_by_filename(
            out_top, tags=self.tags[self.artifact_map["BaseComplexTopologyFile"]]
        )
        art_rst7 = ArtifactRegistry.create_instance_by_filename(
            out_rst7, tags=self.tags[self.artifact_map["BaseComplexStructureFile"]]
        )
        return ArtifactContainer(sysname, (art_top, art_rst7))
