from typing import Optional

import attrs

from amberflow.artifacts import (
    BaseComplexTopologyFile,
    BaseComplexStructureFile,
    BaseComplexStructureReferenceFile,
)
from amberflow.flows import BaseFlow
from amberflow.worknodes import (
    MDRun,
    Filter,
    CreateReferenceStructure,
    MinRestrainedParameters,
    HeatingParameters,
    MDRestrainedParameters,
    MDParameters,
)

__all__ = ("FlowRoeRelaxSingle",)


class FlowRoeRelaxSingle(BaseFlow):
    """
    A flow for an MD relaxation protocol.

    This flow runs a relaxation protocol on a complex systems.
    The protocol involves initial minimization, gradual heating, density equilibration, and a series of steps
    where positional restraints are slowly removed. This is loosely based on the protocol described by Roe [2].

    The first relaxation WorkNodes use the initial input frame as reference, until the first equilibration is completed,
    `density0`, after which it takes the final frame from `density0`, which is the first time the box gets adjusted,
    and it makes it the final reference. After that, all Worknodes get that frame as the reference structure.
    So,
    - clash minimization
    - minimization
    - densitiy 0
    - density 1

    use the initial frame (that came from the previous step) as a reference.
    After that, it's the output frame from density0 that's used as the actual reference structure.
    `density1` kind of does both things, since its input frame and the reference structure are the same thing.


    Parameters
    ----------
    name : str, optional
        The name of the flow instance, by default "relaxroe".
    full_restraint_mask : str
        Amber mask for applying strong restraints on the whole solute during
        the initial clash-fixing minimization.
    noh_restraint_mask : str
        Amber mask for applying restraints on all heavy atoms during heating,
        density equilibration, and initial relaxation stages.
    strong_restraint_wt : int, optional
        The weight (in kcal/mol·Å²) for the strong heavy-atom restraints,
        by default 50.
    bb_restraint_mask : str
        Amber mask for applying restraints on the protein backbone during the
        final relaxation stage.
    bb_restraint_wt : int, optional
        The weight (in kcal/mol·Å²) for the final backbone restraints,
        by default 5.
    relax_weights : tuple[int], optional
        A tuple of integers representing the restraint weights to be used
        in the gradual relaxation stages, by default (25, 10, 5, 2, 1).
    free_restraint_mask : str, optional
        An optional Amber mask to apply during the final free MD run for the complex.
    free_restraint_wt : int, optional
        The restraint weight for the optional final restraint mask for the complex.
    nstlim : int, optional
        The number of MD steps for most of the relaxation stages,
        by default 50000.
    nstlim_density_equilibration : int, optional
        The number of MD steps for the density equilibration stages
        by default 25000.
    maxcyc : int, optional
        The maximum number of minimization cycles, by default 1000.
    ncyc : int, optional
        The number of steepest descent minimization cycles, by default 100.
    skippable : bool, optional
        If True, allows individual worknodes within the flow to be skipped
        if their outputs already exist, by default True.

    References
    ----------
    1. Amber tutorial: https://ambermd.org/tutorials/basic/tutorial13/index.php
    2. Daniel R. Roe, Bernard R. Brooks;
       A protocol for preparing explicitly solvated systems for stable molecular dynamics simulations.
       J. Chem. Phys. 7 August 2020; 153 (5): 054123. https://doi.org/10.1063/5.0013849
    """

    def __init__(
        self,
        name: str = "relaxroesingle",
        *,
        full_restraint_mask: str,
        noh_restraint_mask: str,
        strong_restraint_wt: int = 50,
        bb_restraint_mask: str,
        bb_restraint_wt: int = 5,
        relax_weights: tuple[int] = (25, 10, 5, 2, 1),
        free_restraint_mask: Optional[str] = None,
        free_restraint_wt: Optional[int] = None,
        nstlim: int = 1000000,
        ntpr: int = 1000,
        ntpr_pdt: int = 1000,
        nstlim_density_equilibration: int = 500000,
        maxcyc: int = 1000,
        ncyc: int = 100,
        iwrap: int = 0,
        nscm: int = 0,
        skippable: bool = True,
    ):
        super().__init__(name)

        # Filter initial artifacts
        wnf_top = Filter(
            "wnf_top",
            artifact_types=(BaseComplexTopologyFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_rst = Filter(
            "wnf_rst",
            artifact_types=(BaseComplexStructureFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )

        clash_params = MinRestrainedParameters(ncyc=50, maxcyc=200, restraintmask=full_restraint_mask, restraint_wt=100)
        clash_fix = MDRun(
            "clash_fix",
            mdin_template="min_restrained",
            mdparameters=clash_params,
            engine="pmemd",
            skippable=skippable,
        )

        # Step 1: Minimize heavy atoms
        min_params = MinRestrainedParameters(
            restraintmask=noh_restraint_mask,
            maxcyc=maxcyc,
            ncyc=ncyc,
            restraint_wt=strong_restraint_wt,
        )
        mini = MDRun(
            "mini",
            mdin_template="min_restrained",
            mdparameters=min_params,
            skippable=skippable,
        )

        # Create reference structures for cartesian restraints during this flow
        crs_density0 = CreateReferenceStructure(wnid="crs_density0")

        # Create reference structures for the output
        crs = CreateReferenceStructure(wnid="crs")

        # Filter out the reference that came from the density0 step
        wnf_ref_density0 = Filter(
            "wnf_rst_density0",
            artifact_types=(BaseComplexStructureReferenceFile,),
            in_or_out="out",
            skippable=skippable,
            single=True,
        )

        # Step 2: Heat the system
        heat_params = HeatingParameters(
            nstlim=nstlim,
            ntpr=ntpr,
            restraintmask=noh_restraint_mask,
            restraint_wt=strong_restraint_wt,
        )

        heat = MDRun(
            "heat",
            mdin_template="md_restrained_varying",
            mdparameters=heat_params,
            skippable=skippable,
        )

        # Step 3: Density equilibration
        density_params = MDRestrainedParameters(
            nstlim=nstlim_density_equilibration,  # Reduced nstlim for density equilibration, so pmemd.cuda doesn't complain
            dt=0.001,
            ntpr=ntpr,
            iwrap=iwrap,
            nscm=nscm,
            gamma_ln=2.0,
            restraintmask=noh_restraint_mask,
            restraint_wt=strong_restraint_wt,
            cut=12.0,
        )
        density0 = MDRun(
            "density0",
            mdin_template="md_restrained",
            mdparameters=density_params,
            skippable=skippable,
        )
        density1 = MDRun(
            "density1",
            mdin_template="md_restrained",
            mdparameters=density_params,
            skippable=skippable,
        )

        # Step 4: Gradually reduce restraints
        md_nodes = []
        for i, wt in enumerate(relax_weights):
            md_params = MDRestrainedParameters(
                nstlim=nstlim,
                ntpr=ntpr,
                dt=0.001,
                iwrap=iwrap,
                nscm=nscm,
                gamma_ln=4.0,
                restraintmask=noh_restraint_mask,
                restraint_wt=wt,
            )

            step = MDRun(
                f"lower{i}",
                mdin_template="md_restrained",
                mdparameters=md_params,
                skippable=skippable,
            )
            md_nodes.append(step)

        # Step 5: Final relaxation with backbone restraints
        final_params = MDRestrainedParameters(
            nstlim=nstlim,
            ntpr=ntpr,
            dt=0.002,
            gamma_ln=5.0,
            ntwx=250,
            iwrap=iwrap,
            nscm=nscm,
            restraintmask=bb_restraint_mask,
            restraint_wt=bb_restraint_wt,
        )
        bb = MDRun(
            "bb",
            mdin_template="md_restrained",
            mdparameters=final_params,
            skippable=skippable,
        )
        # Step 6: Free MD
        free_params = MDParameters(
            nstlim=nstlim,
            ntpr=ntpr_pdt,
            dt=0.004,
            gamma_ln=5.0,
            ntwx=250,
            iwrap=iwrap,
            nscm=nscm,
        )
        if None in (free_restraint_mask, free_restraint_wt):
            mdin_template = "md"
        else:
            free_params = attrs.evolve(free_params, restraintmask=free_restraint_mask, restraint_wt=free_restraint_wt)
            mdin_template = "md_restrained"

        free = MDRun(
            "free",
            mdin_template=mdin_template,
            mdparameters=free_params,
            skippable=skippable,
        )

        # Connect the workflow
        self.dag.add_edge(self.root, wnf_top)
        self.dag.add_edge(self.root, wnf_rst)

        self.dag.add_edge(wnf_top, clash_fix)
        self.dag.add_edge(wnf_rst, clash_fix)
        self.dag.add_edge(clash_fix, mini)

        self.dag.add_edge(mini, heat)
        self.dag.add_edge(heat, density0)
        self.dag.add_edge(density0, crs_density0)
        self.dag.add_edge(density0, density1)
        self.dag.add_edge(crs_density0, density1)

        # Restraints relaxation steps may vary
        previous_step = density1
        for step in md_nodes:
            self.dag.add_edge(previous_step, step)
            previous_step = step
        self.dag.add_edge(previous_step, bb)
        self.dag.add_edge(bb, free)

        # Connect to leaf
        self.dag.add_edge(free, wnf_ref_density0)
        self.dag.add_edge(wnf_ref_density0, self.leaf)
        self.dag.add_edge(self.root, crs)
        self.dag.add_edge(crs, self.leaf)
