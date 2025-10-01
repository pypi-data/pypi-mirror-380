from typing import Optional, Sequence

import attrs

from amberflow.artifacts import (
    BaseComplexTopologyFile,
    BaseBinderTopologyFile,
    ComplexProteinLigandRestart,
    BoreschRestraints,
    BaseComplexStructureReferenceFile,
    BaseBinderStructureReferenceFile,
    BinderLigandRestart,
    LambdaScheduleFile,
)
from amberflow.flows import BaseFlow
from amberflow.worknodes import (
    QuickLambdaSchedule,
    AnhilateParameters,
    LambdaParameters,
    LambdaAnhilation,
    LambdaMDRun,
    Amber2Dats,
    GetXML,
    EdgeMBAR,
    Filter,
    GenerateLambdaScheduleFile,
    ImpossibleFilter,
    FEDataExporter,
    AnalysisJSONDataExporter,
)

__all__ = ("FlowABFE7",)


class FlowABFE7(BaseFlow):
    """
    An end-to-end flow for Alchemical Free Energy (AFE) calculations.

    This flow orchestrates the entire AFE workflow for both a complex and a
    ligand system. It begins by preparing the systems (annihilation), then
    runs a multi-stage MD simulation (heating, equilibration, production)
    across a series of lambda windows. Finally, it post-processes the
    trajectories and performs MBAR analysis to calculate the free energy.

    The ligand is assumed to be the first residue in the complex topology.

    Parameters
    ----------
    name : str, optional
        The name of the flow instance (default: "abfe1").

    -- Lambda Schedule --
    binder_nlambdas : int, optional
        Number of lambda windows for the binder. Used if `binder_windows` is
        not set (default: None).
    binder_schedule : str, optional
        The lambda schedule type for the binder (default: "s2inverse").
    complex_nlambdas : int, optional
        Number of lambda windows for the complex. Used if `complex_windows`
        is not set (default: None).
    complex_schedule : str, optional
        The lambda schedule type for the complex (default: "s2inverse").
    binder_windows : Sequence[float], optional
        A specific sequence of lambda values for the binder. Overrides
        `binder_nlambdas` and `binder_schedule` (default: None).
    complex_windows : Sequence[float], optional
        A specific sequence of lambda values for the complex. Overrides

    -- Heating Restraints --
    heating_restraint_mask : str
        Amber mask for applying restraints during the heating phase.
    heating_restraint_wt : int, optional
        Weight for the heating restraints in kcal/mol*A^2 (default: 5).

    -- Complex-Specific Restraints --
    complex_restraint_mask : str, optional
        Amber mask for positional restraints on the complex during
        equilibration (default: None).
    complex_restraint_wt : int, optional
        Weight for the complex positional restraints (default: None).
    nmropt : bool, optional
        If True, enables NMR restraints (e.g., Boresch) for the complex
        system (default: False).

    -- RMSD Restraints (Complex) --
    complex_rmsd_mask : str, optional
        Amber mask for a single RMSD restraint on the complex (default: None).
    complex_rmsd_strength_heat : float, optional
        Strength for the single RMSD restraint on the complex during heating
        (default: 5).
    complex_rmsd_strength_equil1 : float, optional
        Strength for the single RMSD restraint on the complex during first
        equilibration (default: 5).
    complex_rmsd_strength_equil2 : float, optional
        Strength for the single RMSD restraint on the complex during second
        equilibration (default: 5).
    complex_rmsd_strength_trial_equil : float, optional
        Strength for the single RMSD restraint on the complex during trial
        equilibration (default: 5).
    complex_rmsd_strength_trial : float, optional
        Strength for the single RMSD restraint on the complex during trial
        production (default: 5).
    complex_rmsd_ti : int, optional
        Pulling factor for the single RMSD restraint (default: 2).
    complex_rmsd_mask1 : str, optional
        Amber mask for the first of a dual RMSD restraint pair (default: None).
    complex_rmsd_strength1_heat : float, optional
        Strength for the first dual RMSD restraint during heating (default: 2).
    complex_rmsd_strength1_equil1 : float, optional
        Strength for the first dual RMSD restraint during first equilibration
        (default: 3).
    complex_rmsd_strength1_equil2 : float, optional
        Strength for the first dual RMSD restraint during second equilibration
        (default: 4).
    complex_rmsd_strength1_trial_equil : float, optional
        Strength for the first dual RMSD restraint during trial equilibration
        (default: 6).
    complex_rmsd_strength1_trial : float, optional
        Strength for the first dual RMSD restraint during trial production
        (default: 7).
    complex_rmsd_ti1 : int, optional
        Pulling factor for the first dual RMSD restraint (default: 2).
    complex_rmsd_mask2 : str, optional
        Amber mask for the second of a dual RMSD restraint pair (default: None).
    complex_rmsd_strength2_heat : float, optional
        Strength for the second dual RMSD restraint during heating (default: 5).
    complex_rmsd_strength2_equil1 : float, optional
        Strength for the second dual RMSD restraint during first equilibration
        (default: 5).
    complex_rmsd_strength2_equil2 : float, optional
        Strength for the second dual RMSD restraint during second equilibration
        (default: 5).
    complex_rmsd_strength2_trial_equil : float, optional
        Strength for the second dual RMSD restraint during trial equilibration
        (default: 5).
    complex_rmsd_strength2_trial : float, optional
        Strength for the second dual RMSD restraint during trial production
        (default: 5).
    complex_rmsd_ti2 : int, optional
        Pulling factor for the second dual RMSD restraint (default: 1).
    complex_rmsd_type : int, optional
        Type of RMSD restraint for the complex (default: 0).

    -- RMSD Restraints (Binder) --
    binder_rmsd_mask : str, optional
        Amber mask for a single RMSD restraint on the binder (default: None).
    binder_rmsd_strength_heat : float, optional
        Strength for the single RMSD restraint on the binder during heating
        (default: 2).
    binder_rmsd_strength_equil1 : float, optional
        Strength for the single RMSD restraint on the binder during first
        equilibration (default: 3).
    binder_rmsd_strength_equil2 : float, optional
        Strength for the single RMSD restraint on the binder during second
        equilibration (default: 4).
    binder_rmsd_strength_trial_equil : float, optional
        Strength for the single RMSD restraint on the binder during trial
        equilibration (default: 6).
    binder_rmsd_strength_trial : float, optional
        Strength for the single RMSD restraint on the binder during trial
        production (default: 7).
    binder_rmsd_ti : int, optional
        Pulling factor for the single RMSD restraint (default: 2).
    binder_rmsd_mask1 : str, optional
        Amber mask for the first of a dual RMSD restraint pair (default: None).
    binder_rmsd_strength1_heat : float, optional
        Strength for the first dual RMSD restraint during heating (default: 2).
    binder_rmsd_strength1_equil1 : float, optional
        Strength for the first dual RMSD restraint during first equilibration
        (default: 3).
    binder_rmsd_strength1_equil2 : float, optional
        Strength for the first dual RMSD restraint during second equilibration
        (default: 4).
    binder_rmsd_strength1_trial_equil : float, optional
        Strength for the first dual RMSD restraint during trial equilibration
        (default: 6).
    binder_rmsd_strength1_trial : float, optional
        Strength for the first dual RMSD restraint during trial production
        (default: 7).
    binder_rmsd_ti1 : int, optional
        Pulling factor for the first dual RMSD restraint (default: 2).
    binder_rmsd_mask2 : str, optional
        Amber mask for the second of a dual RMSD restraint pair (default: None).
    binder_rmsd_strength2_heat : float, optional
        Strength for the second dual RMSD restraint during heating (default: 2).
    binder_rmsd_strength2_equil1 : float, optional
        Strength for the second dual RMSD restraint during first equilibration
        (default: 3).
    binder_rmsd_strength2_equil2 : float, optional
        Strength for the second dual RMSD restraint during second equilibration
        (default: 4).
    binder_rmsd_strength2_trial_equil : float, optional
        Strength for the second dual RMSD restraint during trial equilibration
        (default: 6).
    binder_rmsd_strength2_trial : float, optional
        Strength for the second dual RMSD restraint during trial production
        (default: 7).
    binder_rmsd_ti2 : int, optional
        Pulling factor for the second dual RMSD restraint (default: 1).
    binder_rmsd_type : int, optional
        Type of RMSD restraint for the binder (default: 0).

    -- Simulation Steps --
    nstlim_heat : int, optional
        Number of steps for lambda heating runs (default: 100000).
    nstlim_equil1 : int, optional
        Number of steps for the first equilibration phase (2fs) (default: 50000).
    nstlim_equil2 : int, optional
        Number of steps for the second equilibration phase (4fs) (default: 250000).
    nstlim_trial_equil : int, optional
        Number of steps for the equilibration phase of each trial (default: 25000).
    nstlim_trial : int, optional
        Number of steps for the production MD run of each trial (default: 125).
    ntpr_trial : int, optional
        Frequency for printing to MD log during production (default: 125).
    ntwx_trial: int, optional
        Frequency for writing trajectory during production (default: 0).
    numexchg : int, optional
        Number of exchange attempts between lambda windows (default: 10000).

    -- Execution & Trials --
    max_systems_binder : int, optional
        Max number of binder systems to run in parallel. Overrides `gpus_binder`
        unless set to 0 (default: 1).
    gpus_binder: int, optional
        Number of GPUs for the binder `LambdaMDRun` worknodes. Is overridden
        by `max_systems_binder` if it is not 0 (default: 1).
    max_systems_complex : int, optional
        Max number of complex systems to run in parallel. Overrides
        `gpus_complex` unless set to 0 (default: 1).
    gpus_complex: int, optional
        Number of GPUs for the complex `LambdaMDRun` worknodes. Is overridden
        by `max_systems_complex` if it is not 0 (default: 1).
    start_trial: int, optional
        The starting trial number (inclusive) (default: 1).
    end_trial: int, optional
        The ending trial number (inclusive) (default: 1).
    skippable : bool, optional
        If True, allows individual worknodes to be skipped if their outputs
        already exist (default: True).

    -- Analysis --
    bar_intervall : int, optional
        Interval for MBAR analysis. If None, defaults to `nstlim_trial`
        (default: None).
    edgembar_mode: str, optional
        The calculation mode for EdgeMBAR, e.g., "BAR" or "MBAR" (default: "BAR").
    skip_analysis : bool, optional
        If True, skips the final analysis steps (default: False).
    """

    def __init__(
        self,
        name: str = "abfe7",
        *,
        binder_nlambdas: int = 12,
        binder_schedule: str = "s2inverse",
        complex_nlambdas: int = 12,
        complex_schedule: str = "s2inverse",
        binder_windows: Optional[Sequence[float]] = None,
        complex_windows: Optional[Sequence[float]] = None,
        heating_restraint_mask: str,
        heating_restraint_wt: int = 5,
        complex_restraint_mask: Optional[str] = None,
        complex_restraint_wt: Optional[int] = None,
        complex_rmsd_mask: Optional[str] = None,
        complex_rmsd_strength_heat: float = 5,
        complex_rmsd_strength_equil1: float = 5,
        complex_rmsd_strength_equil2: float = 5,
        complex_rmsd_strength_trial_equil: float = 5,
        complex_rmsd_strength_trial: float = 5,
        complex_rmsd_ti: int = 2,
        complex_rmsd_mask1: Optional[str] = None,
        complex_rmsd_strength1_heat: float = 2,
        complex_rmsd_strength1_equil1: float = 3,
        complex_rmsd_strength1_equil2: float = 4,
        complex_rmsd_strength1_trial_equil: float = 6,
        complex_rmsd_strength1_trial: float = 7,
        complex_rmsd_ti1: int = 2,
        complex_rmsd_mask2: Optional[str] = None,
        complex_rmsd_strength2_heat: float = 5,
        complex_rmsd_strength2_equil1: float = 5,
        complex_rmsd_strength2_equil2: float = 5,
        complex_rmsd_strength2_trial_equil: float = 5,
        complex_rmsd_strength2_trial: float = 5,
        complex_rmsd_ti2: int = 1,
        complex_rmsd_type: int = 0,
        binder_rmsd_mask: Optional[str] = None,
        binder_rmsd_strength_heat: float = 2,
        binder_rmsd_strength_equil1: float = 3,
        binder_rmsd_strength_equil2: float = 4,
        binder_rmsd_strength_trial_equil: float = 6,
        binder_rmsd_strength_trial: float = 7,
        binder_rmsd_ti: int = 2,
        binder_rmsd_mask1: Optional[str] = None,
        binder_rmsd_strength1_heat: float = 2,
        binder_rmsd_strength1_equil1: float = 3,
        binder_rmsd_strength1_equil2: float = 4,
        binder_rmsd_strength1_trial_equil: float = 6,
        binder_rmsd_strength1_trial: float = 7,
        binder_rmsd_ti1: int = 2,
        binder_rmsd_mask2: Optional[str] = None,
        binder_rmsd_strength2_heat: float = 2,
        binder_rmsd_strength2_equil1: float = 3,
        binder_rmsd_strength2_equil2: float = 4,
        binder_rmsd_strength2_trial_equil: float = 6,
        binder_rmsd_strength2_trial: float = 7,
        binder_rmsd_ti2: int = 1,
        binder_rmsd_type: int = 0,
        nstlim_heat: int = 100000,
        nstlim_equil1: int = 50000,
        nstlim_equil2: int = 250000,
        nstlim_trial_equil: int = 25000,
        nstlim_trial: int = 125,
        ntpr_trial: int = 125,
        ntwx_trial: int = 0,
        bar_intervall: Optional[int] = None,
        numexchg: int = 10000,
        nmropt: bool = False,
        edgembar_mode: str = "BAR",
        max_systems_binder: int = 1,
        gpus_binder: int = 1,
        max_systems_complex: int = 1,
        gpus_complex: int = 1,
        start_trial: int = 1,
        end_trial: int = 1,
        skippable: bool = True,
        skip_analysis: bool = False,
    ):
        super().__init__(name)
        if bar_intervall is None:
            bar_intervall = nstlim_trial
        if (end_trial - start_trial) < 0:
            raise ValueError(f"The number of end_trial must be at least 1. Got {start_trial=} and {end_trial=}.")
        # Set all parameters as attributes
        for name, value in locals().items():
            if name != "self":
                setattr(self, name, value)

        # Filter for the final relaxed structures and topologies
        wnf_binder_top = Filter(
            f"wnf_binder_top_{self.name}",
            artifact_types=(BaseBinderTopologyFile,),
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_binder_rst = Filter(
            f"wnf_binder_rst_{self.name}",
            artifact_types=(BinderLigandRestart,),
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_complex_top = Filter(
            f"wnf_complex_top_{self.name}",
            artifact_types=(BaseComplexTopologyFile,),
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_complex_rst = Filter(
            f"wnf_complex_rst_{self.name}",
            artifact_types=(ComplexProteinLigandRestart,),
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_complex_ref = Filter(
            "wnf_complex_lambda_ref",
            artifact_types=(BaseComplexStructureReferenceFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_binder_ref = Filter(
            "wnf_binder_lambda_ref",
            artifact_types=(BaseBinderStructureReferenceFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_complex_nmr_restraints = Filter(
            "wnf_complex_nmr_restraints",
            artifact_types=(BoreschRestraints,),
            fail_if_no_artifacts=True,
            single=True,
        )
        restrained_str = (
            "_restrained" if complex_restraint_mask is not None and complex_restraint_wt is not None else ""
        )
        nmropt_str = "_nmropt" if nmropt else ""

        complex_rmsd_str = self._setup_rmsd(complex_rmsd_mask, complex_rmsd_mask1, complex_rmsd_mask2)
        binder_rmsd_str = self._setup_rmsd(binder_rmsd_mask, binder_rmsd_mask1, binder_rmsd_mask2)

        # Lambda schedule generation
        if binder_windows is None:
            qls_binder = QuickLambdaSchedule(
                wnid=f"qls_binder_{self.name}", nlambdas=binder_nlambdas, schedule=binder_schedule
            )
        else:
            qls_binder = QuickLambdaSchedule(wnid=f"qls_binder_{self.name}", lambdas=binder_windows)
        if complex_windows is None:
            qls_complex = QuickLambdaSchedule(
                wnid=f"qls_complex_{self.name}", nlambdas=complex_nlambdas, schedule=complex_schedule
            )
        else:
            qls_complex = QuickLambdaSchedule(wnid=f"qls_complex_{self.name}", lambdas=complex_windows)

        # Annihilation step
        anhilate_params = AnhilateParameters(timask1=":1", timask2="", scmask1=":1", scmask2="")

        anhilate_binder = LambdaAnhilation(
            wnid=f"anhilate_binder_{self.name}",
            mdin_template="min_icfe",
            mdparameters=anhilate_params,
            engine="pmemd.cuda",
            skippable=skippable,
        )

        anhilate_complex = LambdaAnhilation(
            wnid=f"anhilate_complex_{self.name}",
            mdin_template=f"min_icfe{restrained_str}{nmropt_str}",
            mdparameters=anhilate_params,
            engine="pmemd.cuda",
            skippable=skippable,
        )

        # Generate LambdaScheduleFile
        lsf = LambdaScheduleFile(
            lambda_type="TypeRestBA",
            function_type="smooth_step2",
            match_type="symmetric",
            parameter1=1.0,
            parameter2=0.0,
        )
        glsch = GenerateLambdaScheduleFile(
            wnid=f"gen_lambda_schedule_file_{self.name}",
            schedules=[lsf],
        )

        # Heating
        heat_params = LambdaParameters(
            nstlim=nstlim_heat,
            irest=0,
            ntx=1,
            timask1=":1",
            timask2="",
            scmask1=":1",
            scmask2="",
            iwrap=0,
            dt=0.001,
            tempi=200,
            temp0=298,
            restraintmask=heating_restraint_mask,
            restraint_wt=heating_restraint_wt,
        )
        # Get the binder MD parameters
        binder_heat_params = self._evolve_rmsd_params(heat_params, environment="binder", stage="heat")
        heat_binder = LambdaMDRun(
            wnid=f"heat_binder_{self.name}",
            mdin_template=f"md_icfe{binder_rmsd_str}_varying",
            engine="pmemd.cuda.MPI",
            mdparameters=binder_heat_params,
            max_systems=max_systems_binder,
            gpus=gpus_binder,
            skippable=skippable,
        )

        # Get the complex MD parameters
        complex_heat_params = self._evolve_rmsd_params(heat_params, environment="complex", stage="heat")
        heat_complex = LambdaMDRun(
            wnid=f"heat_complex_{self.name}",
            mdin_template=f"md_icfe{restrained_str}{complex_rmsd_str}{nmropt_str}_varying",
            ifmbar=True,
            engine="pmemd.cuda.MPI",
            mdparameters=complex_heat_params,
            max_systems=max_systems_complex,
            gpus=gpus_complex,
            skippable=skippable,
        )

        ### Equilibration ###
        # 1 #
        equil1_params = LambdaParameters(
            nstlim=nstlim_equil1,
            irest=1,
            ntx=5,
            timask1=":1",
            timask2="",
            scmask1=":1",
            scmask2="",
            iwrap=0,
            dt=0.002,
            numexchg=numexchg,
        )

        binder_equil1_params = self._evolve_rmsd_params(equil1_params, environment="binder", stage="equil1")
        equil1_binder = LambdaMDRun(
            wnid=f"equil1_binder_{self.name}",
            mdin_template=f"md_icfe{binder_rmsd_str}",
            engine="pmemd.cuda.MPI",
            mdparameters=binder_equil1_params,
            max_systems=max_systems_binder,
            skippable=skippable,
        )

        if restrained_str != "":
            # noinspection PyTypeChecker
            equil1_params = attrs.evolve(
                equil1_params, restraintmask=complex_restraint_mask, restraint_wt=complex_restraint_wt
            )

        complex_equil1_params = self._evolve_rmsd_params(equil1_params, environment="complex", stage="equil1")
        equil1_complex = LambdaMDRun(
            wnid=f"equil1_complex_{self.name}",
            mdin_template=f"md_icfe{restrained_str}{complex_rmsd_str}{nmropt_str}",
            engine="pmemd.cuda.MPI",
            mdparameters=complex_equil1_params,
            max_systems=max_systems_complex,
            skippable=skippable,
        )

        # 2 #
        equil2_params = LambdaParameters(
            nstlim=nstlim_equil2,
            irest=1,
            ntx=5,
            timask1=":1",
            timask2="",
            scmask1=":1",
            scmask2="",
            iwrap=0,
            dt=0.004,
            numexchg=numexchg,
        )
        binder_equil2_params = self._evolve_rmsd_params(equil2_params, environment="binder", stage="equil2")
        equil2_binder = LambdaMDRun(
            wnid=f"equil2_binder_{self.name}",
            mdin_template=f"md_icfe{binder_rmsd_str}",
            engine="pmemd.cuda.MPI",
            mdparameters=binder_equil2_params,
            max_systems=max_systems_binder,
            skippable=skippable,
        )

        if restrained_str != "":
            # noinspection PyTypeChecker
            equil_params = attrs.evolve(
                equil2_params, restraintmask=complex_restraint_mask, restraint_wt=complex_restraint_wt
            )

        complex_equil2_params = self._evolve_rmsd_params(equil2_params, environment="complex", stage="equil2")
        equil2_complex = LambdaMDRun(
            wnid=f"equil2_complex_{self.name}",
            mdin_template=f"md_icfe{restrained_str}{complex_rmsd_str}{nmropt_str}",
            engine="pmemd.cuda.MPI",
            mdparameters=complex_equil2_params,
            max_systems=max_systems_complex,
            skippable=skippable,
        )

        ##### trials begin #####
        ### trials equilibration
        trial_equil_params = LambdaParameters(
            nstlim=nstlim_trial_equil,
            irest=0,
            ntx=1,
            timask1=":1",
            timask2="",
            scmask1=":1",
            scmask2="",
            iwrap=0,
            dt=0.004,
            numexchg=numexchg,
        )
        binder_equil_params = self._evolve_rmsd_params(trial_equil_params, environment="binder", stage="trial_equil")
        complex_equil_params = self._evolve_rmsd_params(trial_equil_params, environment="complex", stage="trial_equil")
        ### trials production
        pdt_params = attrs.evolve(
            trial_equil_params,
            nstlim=nstlim_trial,
            bar_intervall=bar_intervall,
            ntpr=ntpr_trial,
            ntwx=ntwx_trial,
        )
        binder_pdt_params = self._evolve_rmsd_params(pdt_params, environment="binder", stage="trial")
        complex_pdt_params = self._evolve_rmsd_params(pdt_params, environment="complex", stage="trial")
        #
        tbinder_nodes = []
        tcomplex_nodes = []
        for i in range(start_trial, end_trial + 1):
            # Binder
            tequil_binder = LambdaMDRun(
                wnid=f"t{i}equil_binder_{self.name}",
                mdin_template=f"md_icfe{binder_rmsd_str}",
                engine="pmemd.cuda.MPI",
                mdparameters=binder_equil_params,
                max_systems=max_systems_binder,
                skippable=skippable,
            )
            tpdt_binder = LambdaMDRun(
                wnid=f"t{i}_binder_{self.name}",
                mdin_template=f"ti_exch_mbar{binder_rmsd_str}",
                ifmbar=True,
                exchange=True,
                engine="pmemd.cuda.MPI",
                mdparameters=binder_pdt_params,
                max_systems=max_systems_binder,
                skippable=skippable,
            )
            tbinder_nodes.append((tequil_binder, tpdt_binder))

            # Complex
            tequil_complex = LambdaMDRun(
                wnid=f"t{i}equil_complex_{self.name}",
                mdin_template=f"md_icfe{restrained_str}{complex_rmsd_str}{nmropt_str}",
                engine="pmemd.cuda.MPI",
                mdparameters=complex_equil_params,
                max_systems=max_systems_complex,
                skippable=skippable,
            )
            tpdt_complex = LambdaMDRun(
                wnid=f"t{i}_complex_{self.name}",
                mdin_template=f"ti_exch_mbar{restrained_str}{complex_rmsd_str}{nmropt_str}",
                ifmbar=True,
                exchange=True,
                engine="pmemd.cuda.MPI",
                mdparameters=complex_pdt_params,
                max_systems=max_systems_complex,
                skippable=skippable,
            )
            tcomplex_nodes.append((tequil_complex, tpdt_complex))

        # Post-processing and analysis
        a2d = Amber2Dats(wnid=f"a2d_{self.name}", skippable=skip_analysis)
        xml = GetXML(wnid=f"xml_{self.name}", skippable=skip_analysis)
        mbar = EdgeMBAR(wnid=f"edge_mbar_{self.name}", mode=edgembar_mode, skippable=skip_analysis)
        create_csv = FEDataExporter(wnid=f"fe_analysis_{self.name}", skippable=skip_analysis)
        create_json = AnalysisJSONDataExporter(wnid=f"json_analysis_{self.name}", skippable=skip_analysis)

        # Connect the workflow
        self.dag.add_edge(self.root, wnf_binder_top)
        self.dag.add_edge(self.root, wnf_binder_rst)
        self.dag.add_edge(self.root, wnf_complex_top)
        self.dag.add_edge(self.root, wnf_complex_rst)
        self.dag.add_edge(self.root, wnf_complex_ref)
        self.dag.add_edge(self.root, wnf_binder_ref)
        self.dag.add_edge(self.root, qls_binder)
        self.dag.add_edge(self.root, qls_complex)
        self.dag.add_edge(self.root, glsch)
        if nmropt:
            self.dag.add_edge(self.root, wnf_complex_nmr_restraints)

        # Binder path
        # Anhilation
        self.dag.add_edge(wnf_binder_top, anhilate_binder)
        self.dag.add_edge(wnf_binder_rst, anhilate_binder)
        self.dag.add_edge(qls_binder, anhilate_binder)
        # Heating
        self.dag.add_edge(anhilate_binder, heat_binder)
        self.dag.add_edge(wnf_binder_ref, heat_binder)
        # Equilibration
        self.dag.add_edge(heat_binder, equil1_binder)
        self.dag.add_edge(equil1_binder, equil2_binder)
        # Trials
        for tequil_binder, tpdt_binder in tbinder_nodes:
            self.dag.add_edge(equil2_binder, tequil_binder)
            self.dag.add_edge(tequil_binder, tpdt_binder)
            self.dag.add_edge(tpdt_binder, a2d)

        # Complex path
        # Anhilation
        if nmropt:
            self.dag.add_edge(wnf_complex_nmr_restraints, anhilate_complex)
        self.dag.add_edge(wnf_complex_top, anhilate_complex)
        self.dag.add_edge(wnf_complex_rst, anhilate_complex)
        self.dag.add_edge(qls_complex, anhilate_complex)
        # Heating
        self.dag.add_edge(anhilate_complex, heat_complex)
        self.dag.add_edge(glsch, heat_complex)
        self.dag.add_edge(wnf_complex_ref, heat_complex)
        # Equilibration
        self.dag.add_edge(heat_complex, equil1_complex)
        self.dag.add_edge(equil1_complex, equil2_complex)
        # Trials
        for tequil_complex, tpdt_complex in tcomplex_nodes:
            self.dag.add_edge(equil2_complex, tequil_complex)
            self.dag.add_edge(tequil_complex, tpdt_complex)
            self.dag.add_edge(tpdt_complex, a2d)
        # Analysis path
        self.dag.add_edge(a2d, xml)
        self.dag.add_edge(xml, mbar)
        self.dag.add_edge(mbar, create_json)
        self.dag.add_edge(mbar, create_csv)
        self.dag.add_edge(mbar, self.leaf)
        self.dag.add_edge(create_json, self.leaf)
        self.dag.add_edge(create_csv, self.leaf)

        ###### quick analysis on each trial ######
        tequils = []
        tpdts = []
        for tbinder, tcomplex in zip(tbinder_nodes, tcomplex_nodes):
            tequils.append((tbinder[0], tcomplex[0]))
            tpdts.append((tbinder[1], tcomplex[1]))
        tmbar_nodes = []
        for j, (tpdt_binder, tpdt_complex) in enumerate(tpdts, start=start_trial):
            ta2d = Amber2Dats(wnid=f"a2d{j}_{self.name}", skippable=skip_analysis)
            self.dag.add_edge(tpdt_binder, ta2d)
            self.dag.add_edge(tpdt_complex, ta2d)
            txml = GetXML(wnid=f"xml{j}_{self.name}", skippable=skip_analysis)
            self.dag.add_edge(ta2d, txml)
            tmbar = EdgeMBAR(wnid=f"edge_mbar{j}_{self.name}", mode=edgembar_mode, skippable=skip_analysis)
            self.dag.add_edge(txml, tmbar)
            tmbar_nodes.append(tmbar)

        ###### Add job dependencies between trials, so they each complete before the next one starts ######
        for j, (tequil_binder, tequil_complex) in enumerate(tequils[1:]):
            blockt = ImpossibleFilter(wnid=f"blockt{start_trial + j + 1}_{self.name}")
            self.dag.add_edge(tmbar_nodes[j], blockt)
            self.dag.add_edge(blockt, tequil_binder)
            self.dag.add_edge(blockt, tequil_complex)

    @staticmethod
    def _setup_rmsd(rmsd_mask, rmsd_mask1, rmsd_mask2) -> str:
        if rmsd_mask is not None:
            return "_rmsd"
        elif rmsd_mask1 is not None and rmsd_mask2 is not None:
            return "_rmsd2"
        else:
            return ""

    def _get_rmsd_kwargs(self, prefix: str, stage: str) -> dict:
        """Helper to get rmsd attributes based on a prefix."""
        attr_suffixes = [
            "rmsd_mask",
            "rmsd_strength",
            "rmsd_ti",
            "rmsd_mask1",
            "rmsd_strength1",
            "rmsd_ti1",
            "rmsd_mask2",
            "rmsd_strength2",
            "rmsd_ti2",
            "rmsd_type",
        ]

        # Build the keyword arguments dynamically
        kwargs = {}
        for suffix in attr_suffixes:
            if suffix.split("_")[1].startswith("strength"):
                kwargs[suffix] = getattr(self, f"{prefix}_{suffix}_{stage}")
            else:
                kwargs[suffix] = getattr(self, f"{prefix}_{suffix}")
        return kwargs

    def _evolve_rmsd_params(self, params: LambdaParameters, *, environment: str, stage: str) -> LambdaParameters:
        kwargs = self._get_rmsd_kwargs(environment, stage)
        return attrs.evolve(params, **kwargs)
