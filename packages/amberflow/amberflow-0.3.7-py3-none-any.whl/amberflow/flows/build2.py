from typing import Optional

from amberflow.artifacts import (
    BaseTargetStructureFile,
    LigandFrcmod,
    LigandLib,
    BaseComplexStructureFile,
    BaseBinderStructureFile,
    BinderLigandRestart,
    ComplexProteinLigandRestart,
    BinderLigandMol2,
)
from amberflow.artifacts.md import BaseComplexPeriodicBox, BaseBinderPeriodicBox
from amberflow.flows import BaseFlow
from amberflow.worknodes import (
    Filter,
    AddChainid,
    JoinTargetBinder,
    BuildAFEBoxes,
    GenerateTopology,
    HMR,
    FFPOPT,
    CreateReferenceStructure,
)

__all__ = ("FlowBuild2",)


class FlowBuild2(BaseFlow):
    """
    This forms the complex, builds 1 box for all the systems, generates the topologies,
    performs Hydrogen Mass Repartition on both the target and the binder topologies, and optionally runs FFopt
    to fix the binder rotamers.

    Parameters
    ----------
    name : str, optional
        The name of the flow instance, Default: "build".

    to_guess : tuple, optional
        Topology attributes for MDAnalysis to guess when joining the target and binder, used by `JoinTargetBinder`
        and `BuildAFEBoxes`. Default: ("elements",).
    renumber : bool, optional
        Whether to renumber residues sequentially after joining, used by `JoinTargetBinder`. Default: True.
    solvent : str, optional
        The water model to use for solvation in `BuildAFEBoxes` and `GenerateTopology`. Default: "tip4pew".
    ions : str, optional
        The ion model to use in `GenerateTopology`. Default: "jc".
    boxshape : str, optional
        The shape of the periodic box (`truncated_octahedron` or `orthorhombic`) to be specified in `BuildAFEBoxes`.
        Default: "truncated_octahedron".
    boxshape_gtc: str, optional
        The shape of the periodic box (`truncated_octahedron` or `orthorhombic`) to be specified in `GenerateTopology`.
        Default: "truncated_octahedron". If `None`, the "solvate<box|oct>" statement in Tleap is not used. This affects
        centering of the system.
    skippable : bool, optional
        If True, allows individual worknodes within the flow to be skipped if their outputs already exist.
        Default: True.
    ffopt : bool, optional
        If True, add a final WorkNode to fix ligand rotamers.
        Works only if the binder ligand has an anionic amide group.
        Default: True.
    """

    def __init__(
        self,
        name: str = "build1",
        to_guess: tuple = ("elements",),
        renumber: bool = True,
        solvent: str = "tip4pew",
        ions: str = "jc",
        boxshape: str = "truncated_octahedron",
        boxshape_gtc: Optional[str] = "truncated_octahedron",
        ffopt: bool = True,
        skippable: bool = True,
    ):
        super().__init__(name)

        wnf_binder_parameters = Filter(
            wnid=f"wnf_binder_parameters_{self.name}",
            artifact_types=(BinderLigandMol2, LigandFrcmod, LigandLib, BaseBinderStructureFile),
            skippable=skippable,
            fail_if_no_artifacts=True,
        )
        wnf1 = Filter(
            wnid=f"wnf1_{self.name}",
            artifact_types=(BaseTargetStructureFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        addchainid = AddChainid(wnid=f"addchainid_{self.name}", skippable=skippable)
        jtb = JoinTargetBinder(wnid=f"jtb_{self.name}", to_guess=to_guess, renumber=renumber, skippable=skippable)
        bafeb = BuildAFEBoxes(
            wnid=f"bafeb_{self.name}", to_guess=to_guess, solvent=solvent, boxshape=boxshape, skippable=skippable
        )
        wnf2 = Filter(wnid=f"wnf2_{self.name}", artifact_types=(LigandFrcmod, LigandLib), skippable=skippable)
        wnf3_complex = Filter(
            wnid=f"wnf3_complex_{self.name}",
            artifact_types=(BaseComplexStructureFile, BaseComplexPeriodicBox),
            skippable=skippable,
        )
        gtc = GenerateTopology(
            wnid=f"gtc_{self.name}", solvent=solvent, ions=ions, boxshape=boxshape_gtc, skippable=skippable
        )
        # Take the .rst7 from `gtc` to create the reference structure for the complex.
        crs_complex = CreateReferenceStructure(wnid=f"crs_complex_{self.name}")

        wnf3_binder = Filter(
            wnid=f"wnf3_binder_{self.name}",
            artifact_types=(BaseBinderStructureFile, BaseBinderPeriodicBox),
            skippable=skippable,
        )
        gtb = GenerateTopology(
            wnid=f"gtb_{self.name}", solvent=solvent, ions=ions, boxshape=boxshape_gtc, skippable=skippable
        )
        # Take the .rst7 from `gtb` to create the reference structure for the binder.
        crs_binder = CreateReferenceStructure(wnid=f"crs_binder_{self.name}")

        hmr_binder = HMR(wnid=f"hmr_binder_{self.name}", skippable=skippable)
        hmr_complex = HMR(wnid=f"hmr_complex_{self.name}", skippable=skippable)

        ffopt_binder: Optional[FFPOPT] = None
        ffopt_complex: Optional[FFPOPT] = None
        if ffopt:
            ffopt_binder = FFPOPT(wnid=f"ffopt_binder_{self.name}", skippable=skippable)
            ffopt_complex = FFPOPT(wnid=f"ffopt_complex_{self.name}", skippable=skippable)
        wnf_binder = Filter(wnid=f"wnf_binder_{self.name}", artifact_types=(BinderLigandRestart,), skippable=skippable)
        wnf_complex = Filter(
            wnid=f"wnf_complex_{self.name}", artifact_types=(ComplexProteinLigandRestart,), skippable=skippable
        )

        # Start with the root node
        self.dag.add_edge(self.root, wnf_binder_parameters)
        self.dag.add_edge(self.root, wnf1)
        self.dag.add_edge(wnf_binder_parameters, jtb)
        self.dag.add_edge(wnf_binder_parameters, bafeb)
        self.dag.add_edge(wnf_binder_parameters, wnf2)
        self.dag.add_edge(wnf1, addchainid)
        self.dag.add_edge(addchainid, jtb)
        self.dag.add_edge(jtb, bafeb)
        self.dag.add_edge(bafeb, wnf3_complex)
        self.dag.add_edge(bafeb, wnf3_binder)
        self.dag.add_edge(wnf3_complex, gtc)
        self.dag.add_edge(wnf2, gtc)
        self.dag.add_edge(wnf3_binder, gtb)
        self.dag.add_edge(wnf2, gtb)
        self.dag.add_edge(gtc, hmr_complex)
        self.dag.add_edge(gtc, crs_complex)
        self.dag.add_edge(hmr_complex, ffopt_complex)
        self.dag.add_edge(gtb, hmr_binder)
        self.dag.add_edge(gtb, crs_binder)
        self.dag.add_edge(hmr_binder, ffopt_binder)
        self.dag.add_edge(gtb, wnf_binder)
        self.dag.add_edge(gtc, wnf_complex)

        # End with the leaf node
        # `ffopt_complex` (or `hmr_complex`) and `ffopt_binder` (or `hmr_binder`) have the complex and binder topologies, respectively.
        if ffopt:
            self.dag.add_edge(hmr_complex, ffopt_complex)
            self.dag.add_edge(ffopt_complex, self.leaf)

            self.dag.add_edge(hmr_binder, ffopt_binder)
            self.dag.add_edge(ffopt_binder, self.leaf)
        else:
            self.dag.add_edge(hmr_complex, self.leaf)
            self.dag.add_edge(hmr_binder, self.leaf)
        # `wnf_complex` and `wnf_binder` have the complex and binder restarts, respectively.
        self.dag.add_edge(wnf_complex, self.leaf)
        self.dag.add_edge(wnf_binder, self.leaf)
        # Output the reference structures
        self.dag.add_edge(crs_complex, self.leaf)
        self.dag.add_edge(crs_binder, self.leaf)
