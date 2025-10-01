from typing import Optional

from amberflow.artifacts import (
    BaseComplexStructureFile,
    BaseAmberMaskString,
    BinderLigandPDB,
    LigandLib,
    LigandFrcmod,
    BaseBinderLigandStructureFile,
    BinderLigandRestart,
    ComplexProteinLigandRestart,
)
from amberflow.customartifacts import (
    BaseDockComplexStructureFile,
    BaseDockTargetStructureFile,
    BaseDockBinderStructureFile,
    DockBinderLib,
    DockBinderFrcmod,
    BoxBinderLigandPDB,
)
from amberflow.customworknodes import (
    BuildDockTemplate,
    DockRestraints,
    ProcessTimsDocked,
    BoxLigand,
)
from amberflow.flows import BaseFlow
from amberflow.worknodes import (
    GenerateTopology,
    HMR,
    FFPOPT,
    Filter,
    MDRun,
    AnhilateParameters,
    LambdaParameters,
    Ambpdb,
    CreateReferenceStructure,
)

__all__ = ("FlowTimsDocking1",)


class FlowTimsDocking1(BaseFlow):
    def __init__(
        self,
        name: str = "timsdocking1",
        *,
        solvent: str = "tip4pew",
        ions: str = "jv",
        boxshape: str = "truncated_octahedron",
        resolution: float = 0.5,
        solute_radius: float = 1.4,
        solvent_radius: float = 1.1,
        clash_cutoff: float = 3.0,
        nstlim_heat: int = 5000,
        nstlim_equil: int = 5000,
        nstlim_noneq: int = 6000,
        max_systems_binder: int = 1,
        gpus_binder: int = 1,
        max_systems_complex: int = 1,
        gpus_complex: int = 1,
        start_trial: int = 1,
        end_trial: int = 1,
        ffopt: bool = True,
        skippable: bool = True,
    ):
        super().__init__(name)
        if (end_trial - start_trial) < 0:
            raise ValueError(f"The number of end_trial must be at least 1. Got {start_trial=} and {end_trial=}.")
        # Set all parameters as attributes
        for name, value in locals().items():
            if name != "self":
                setattr(self, name, value)

        wnf_inputs = Filter(
            f"wnf_inputs_{self.name}",
            artifact_types=(
                BinderLigandPDB,
                LigandLib,
                LigandFrcmod,
                BaseDockTargetStructureFile,
                BaseDockBinderStructureFile,
                DockBinderLib,
                DockBinderFrcmod,
                BaseBinderLigandStructureFile,
                BoxBinderLigandPDB,
            ),
            fail_if_no_artifacts=True,
            single=True,
        )

        bdt = BuildDockTemplate(wnid=f"bdt_{self.name}", selector="mcs", aligner="rmsdcommoncore")
        gtc = GenerateTopology(
            wnid=f"gtc_{self.name}",
            solvent=solvent,
            ions=ions,
            boxshape=boxshape,
            skippable=skippable,
            neutralize=False,
        )
        hmr = HMR(wnid=f"hmr_{self.name}", skippable=skippable)
        ffopt_complex: Optional[FFPOPT] = None
        if ffopt:
            ffopt_binder = FFPOPT(wnid=f"ffopt_binder_{self.name}", skippable=skippable)
            ffopt_complex = FFPOPT(wnid=f"ffopt_complex_{self.name}", skippable=skippable)
        ffopt = FFPOPT(wnid=f"ffopt_{self.name}", skippable=skippable)
        masks = DockRestraints(wnid=f"masks_{self.name}", skippable=skippable)
        wnf_out_dock = Filter(
            wnid=f"wnf_out_dock_{self.name}",
            artifact_types=(BaseDockComplexStructureFile,),
            in_or_out="out",
            skippable=skippable,
        )
        wnf_in_rst7 = Filter(
            wnid=f"wnf_in_rst7_{self.name}",
            artifact_types=(BaseComplexStructureFile,),
            in_or_out="in",
            skippable=skippable,
        )
        wnf_in_afemask = Filter(
            wnid=f"wnf_in_afemask_{self.name}",
            artifact_types=(BaseAmberMaskString,),
            in_or_out="in",
            skippable=skippable,
        )
        min_params = AnhilateParameters(ncyc=50, maxcyc=250, restraint_wt=50, clambda=0.0, gti_bat_sc=0, gti_add_sc=5)
        init_min = MDRun(
            wnid=f"init_min_{self.name}",
            mdin_template="min_icfe_restrained_nmropt",
            mdparameters=min_params,
            engine="pmemd.cuda",
            skippable=skippable,
        )

        heat_params = LambdaParameters(
            nstlim=nstlim_heat,
            irest=0,
            ntx=1,
            iwrap=0,
            dt=0.001,
            tempi=100,
            temp0=298,
            restraint_wt=50,
            clambda=0.0,
            gti_bat_sc=0,
            gti_add_sc=5,
            gamma_ln=2,
        )
        wnf_in_dockcomplex = Filter(
            wnid=f"wnf_in_dockcomplex_{self.name}",
            artifact_types=(BaseDockComplexStructureFile,),
            in_or_out="in",
            skippable=skippable,
        )
        init_heat = MDRun(
            wnid=f"init_heat_{self.name}",
            mdin_template="md_icfe_restrained_nmropt_varying",
            mdparameters=heat_params,
            engine="pmemd.cuda",
            skippable=skippable,
        )
        equil_params = LambdaParameters(
            nstlim=nstlim_equil,
            irest=1,
            ntx=5,
            iwrap=0,
            dt=0.001,
            temp0=298,
            restraint_wt=50,
            clambda=0.0,
            gamma_ln=2,
        )
        noneq_params = LambdaParameters(
            nstlim=nstlim_noneq,
            irest=1,
            ntx=5,
            iwrap=0,
            dt=0.001,
            temp0=298,
            restraint_wt=50,
            clambda=0.0,
            gamma_ln=2,
            ntave=60,
            dynlmb=0.01,
        )
        min1_params = AnhilateParameters(ncyc=50, maxcyc=200, restraint_wt=50, clambda=1.0, gti_bat_sc=0)

        pt = ProcessTimsDocked(wnid=f"pt_{self.name}")
        ambpdb = Ambpdb(wnid=f"ambpdb_{self.name}")
        crs = CreateReferenceStructure(wnid=f"crs{self.name}")

        for trial in range(start_trial, end_trial + 1):
            equil = MDRun(
                wnid=f"equil_t{trial}_{self.name}",
                mdin_template="md_icfe_restrained_nmropt",
                mdparameters=equil_params,
                engine="pmemd.cuda",
                skippable=skippable,
            )
            noneq = MDRun(
                wnid=f"noneq_t{trial}_{self.name}",
                mdin_template="md_icfe_restrained_nmropt",
                mdparameters=noneq_params,
                engine="pmemd.cuda",
                skippable=skippable,
            )
            min1 = MDRun(
                wnid=f"min1_t{trial}_{self.name}",
                mdin_template="min_icfe_restrained_nmropt",
                mdparameters=min1_params,
                engine="pmemd.cuda",
                skippable=skippable,
            )

            self.dag.add_edge(init_heat, equil)
            self.dag.add_edge(equil, noneq)
            self.dag.add_edge(noneq, min1)
            self.dag.add_edge(min1, pt)

        ########## binder ##########
        bl = BoxLigand(wnid="bl", resolution=resolution, solute_radius=solute_radius, solvent_radius=solvent_radius)
        gtb = GenerateTopology(
            wnid=f"gtb_{self.name}",
            solvent=solvent,
            ions=ions,
            boxshape=boxshape,
            skippable=skippable,
            neutralize=False,
        )
        # Take the .rst7 from `gtb` to create the reference structure for the binder.
        crs_binder = CreateReferenceStructure(wnid=f"crs_binder_{self.name}")

        hmr_binder = HMR(wnid=f"hmr_binder_{self.name}", skippable=skippable)
        hmr_complex = HMR(wnid=f"hmr_complex_{self.name}", skippable=skippable)

        ffopt_binder: Optional[FFPOPT] = None
        if ffopt:
            ffopt_complex = FFPOPT(wnid=f"ffopt_complex_{self.name}", skippable=skippable)
        wnf_binder = Filter(wnid=f"wnf_binder_{self.name}", artifact_types=(BinderLigandRestart,), skippable=skippable)
        wnf_complex = Filter(
            wnid=f"wnf_complex_{self.name}", artifact_types=(ComplexProteinLigandRestart,), skippable=skippable
        )

        self.dag.add_edge(self.root, wnf_inputs)
        self.dag.add_edge(wnf_inputs, bdt)
        self.dag.add_edge(wnf_inputs, bl)

        self.dag.add_edge(bdt, gtc)
        self.dag.add_edge(bdt, wnf_out_dock)
        self.dag.add_edge(bdt, wnf_in_afemask)

        self.dag.add_edge(gtc, hmr)
        self.dag.add_edge(gtc, wnf_in_rst7)

        self.dag.add_edge(wnf_out_dock, masks)
        self.dag.add_edge(wnf_in_afemask, init_min)

        self.dag.add_edge(hmr, ffopt)

        self.dag.add_edge(ffopt, masks)
        self.dag.add_edge(ffopt, init_min)

        self.dag.add_edge(wnf_in_rst7, masks)
        self.dag.add_edge(wnf_in_rst7, init_min)

        self.dag.add_edge(masks, init_min)

        self.dag.add_edge(wnf_in_afemask, init_min)

        self.dag.add_edge(init_min, init_heat)
        self.dag.add_edge(pt, ambpdb)
        self.dag.add_edge(pt, crs)
        self.dag.add_edge(crs, self.leaf)
        self.dag.add_edge(pt, self.leaf)
