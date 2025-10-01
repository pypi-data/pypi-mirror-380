from typing import Optional

import attrs

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
from amberflow.artifacts import (
    BaseComplexTopologyFile,
    BaseBinderTopologyFile,
    BaseBinderStructureFile,
    BaseComplexStructureFile,
    BaseComplexStructureReferenceFile,
    BaseBinderStructureReferenceFile,
)

__all__ = ("FlowRoeRelax2",)


class FlowRoeRelax2(BaseFlow):
    """
    A flow for an MD relaxation protocol.

    This flow runs a relaxation protocol on a pair of complex and ligand
    systems. The protocol involves initial minimization, gradual heating,
    density equilibration, and a series of steps where positional
    restraints are slowly removed. This is loosely based on the protocol
    described by Roe [2].

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
    complex_full_restraint_mask : str
        Amber mask for applying strong restraints on the whole solute during
        the initial clash-fixing minimization.
    complex_noh_restraint_mask : str
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
    complex_free_restraint_mask : str, optional
        An optional Amber mask to apply during the final free MD run for the complex.
    complex_free_restraint_wt : int, optional
        The restraint weight for the optional final restraint mask for the complex.
    nstlim : int, optional
        The number of MD steps for most of the relaxation stages,
        by default 50000.
    nstlim_density_equilibration0 : int, optional
        The number of MD steps for the first density equilibration
        by default 10000.
    nstlim_density_equilibration1 : int, optional
        The number of MD steps for the second density equilibration
        by default 490000.
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
        name: str = "roerelax2",
        *,
        complex_full_restraint_mask: str,
        complex_noh_restraint_mask: str,
        binder_full_restraint_mask: str,
        binder_noh_restraint_mask: str,
        strong_restraint_wt: int = 50,
        bb_restraint_mask: str,
        bb_restraint_wt: int = 5,
        relax_weights: tuple[int] = (25, 10, 5, 2, 1),
        complex_free_restraint_mask: Optional[str] = None,
        complex_free_restraint_wt: Optional[int] = None,
        nstlim: int = 1000000,
        ntpr: int = 1000,
        ntpr_pdt: int = 1000,
        ntwx_pdt: int = 250,
        nstlim_density_equilibration0: int = 10000,
        nstlim_density_equilibration1: int = 490000,
        maxcyc: int = 1000,
        ncyc: int = 100,
        iwrap: int = 0,
        nscm: int = 0,
        skippable: bool = True,
    ):
        super().__init__(name)

        # Filter initial artifacts
        wnf_binder_top = Filter(
            wnid=f"wnf_binder_top_{self.name}",
            artifact_types=(BaseBinderTopologyFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_binder_rst = Filter(
            wnid=f"wnf_binder_rst_{self.name}",
            artifact_types=(BaseBinderStructureFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_binder_ref = Filter(
            wnid=f"wnf_binder_ref_{self.name}",
            artifact_types=(BaseBinderStructureReferenceFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_complex_top = Filter(
            wnid=f"wnf_complex_top_{self.name}",
            artifact_types=(BaseComplexTopologyFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_complex_rst = Filter(
            wnid=f"wnf_complex_rst_{self.name}",
            artifact_types=(BaseComplexStructureFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_complex_ref = Filter(
            wnid=f"wnf_complex_ref_{self.name}",
            artifact_types=(BaseComplexStructureReferenceFile,),
            skippable=skippable,
            fail_if_no_artifacts=True,
            single=True,
        )

        # Relaxation protocol steps
        # Step 0: Very strong restraints on all atoms
        binder_clash0_params = MinRestrainedParameters(
            ncyc=50, maxcyc=200, restraintmask=binder_full_restraint_mask, restraint_wt=100
        )
        clash_fix_binder = MDRun(
            wnid=f"clash_fix_binder_{self.name}",
            mdin_template="min_restrained",
            mdparameters=binder_clash0_params,
            engine="pmemd",
            skippable=skippable,
        )
        complex_clash0_params = attrs.evolve(binder_clash0_params, restraintmask=complex_full_restraint_mask)
        clash_fix_complex = MDRun(
            wnid=f"clash_fix_complex_{self.name}",
            mdin_template="min_restrained",
            mdparameters=complex_clash0_params,
            engine="pmemd",
            skippable=skippable,
        )

        # Step 1: Minimize heavy atoms
        binder_min1_params = MinRestrainedParameters(
            restraintmask=binder_noh_restraint_mask,
            maxcyc=maxcyc,
            ncyc=ncyc,
            restraint_wt=strong_restraint_wt,
        )
        min1_binder = MDRun(
            wnid=f"min_binder_{self.name}",
            mdin_template="min_restrained",
            mdparameters=binder_min1_params,
            skippable=skippable,
        )
        complex_clash0_params = attrs.evolve(binder_min1_params, restraintmask=complex_noh_restraint_mask)
        min1_complex = MDRun(
            wnid=f"min_complex_{self.name}",
            mdin_template="min_restrained",
            mdparameters=complex_clash0_params,
            skippable=skippable,
        )

        # Create reference structures for cartesian restraints during this flow
        crs_density0_complex = CreateReferenceStructure(wnid=f"crs_density0_complex_{self.name}")
        crs_density0_binder = CreateReferenceStructure(wnid=f"crs_density0_binder_{self.name}")

        # Create reference structures for the output
        crs_complex = CreateReferenceStructure(wnid=f"crs_complex_{self.name}")
        crs_binder = CreateReferenceStructure(wnid=f"crs_binder_{self.name}")

        # Filter out the reference that came from the density0 step
        wnf_binder_ref_density0 = Filter(
            wnid=f"wnf_binder_ref_density0_{self.name}",
            artifact_types=(BaseBinderStructureReferenceFile,),
            in_or_out="out",
            skippable=skippable,
            single=True,
        )
        wnf_complex_ref_density0 = Filter(
            wnid=f"wnf_complex_rst_density0_{self.name}",
            artifact_types=(BaseComplexStructureReferenceFile,),
            in_or_out="out",
            skippable=skippable,
            single=True,
        )

        # Step 2: Heat the system
        binder_heat_params = HeatingParameters(
            nstlim=nstlim,
            ntpr=ntpr,
            restraintmask=binder_noh_restraint_mask,
            restraint_wt=strong_restraint_wt,
        )
        heat_binder = MDRun(
            wnid=f"heat_binder_{self.name}",
            mdin_template="md_restrained_varying",
            mdparameters=binder_heat_params,
            skippable=skippable,
        )
        complex_heat_params = attrs.evolve(binder_heat_params, restraintmask=complex_noh_restraint_mask)
        heat_complex = MDRun(
            wnid=f"heat_complex_{self.name}",
            mdin_template="md_restrained_varying",
            mdparameters=complex_heat_params,
            skippable=skippable,
        )

        # Step 3: Density equilibration
        density0_params_binder = MDRestrainedParameters(
            nstlim=nstlim_density_equilibration0,  # Reduced nstlim for density equilibration, so pmemd.cuda doesn't complain
            dt=0.001,
            ntpr=ntpr,
            iwrap=iwrap,
            nscm=nscm,
            gamma_ln=2.0,
            restraintmask=binder_noh_restraint_mask,
            restraint_wt=strong_restraint_wt,
        )
        density0_binder = MDRun(
            wnid=f"density0_binder_{self.name}",
            mdin_template="md_restrained",
            mdparameters=density0_params_binder,
            skippable=skippable,
        )
        density1_params_binder = attrs.evolve(density0_params_binder, nstlim=nstlim_density_equilibration1)
        density1_binder = MDRun(
            wnid=f"density1_binder_{self.name}",
            mdin_template="md_restrained",
            mdparameters=density1_params_binder,
            skippable=skippable,
        )
        density0_params_complex = attrs.evolve(density0_params_binder, restraintmask=complex_noh_restraint_mask)
        density0_complex = MDRun(
            wnid=f"density0_complex_{self.name}",
            mdin_template="md_restrained",
            mdparameters=density0_params_complex,
            skippable=skippable,
        )
        density1_params_complex = attrs.evolve(density1_params_binder, restraintmask=complex_noh_restraint_mask)
        density1_complex = MDRun(
            wnid=f"density1_complex_{self.name}",
            mdin_template="md_restrained",
            mdparameters=density1_params_complex,
            skippable=skippable,
        )

        # Step 4: Gradually reduce restraints
        md_nodes = []
        for i, wt in enumerate(relax_weights):
            md_params_binder = MDRestrainedParameters(
                nstlim=nstlim,
                ntpr=ntpr,
                dt=0.001,
                iwrap=iwrap,
                nscm=nscm,
                gamma_ln=4.0,
                restraintmask=binder_noh_restraint_mask,
                restraint_wt=wt,
            )
            step_binder = MDRun(
                wnid=f"lower{i}_binder_{self.name}",
                mdin_template="md_restrained",
                mdparameters=md_params_binder,
                skippable=skippable,
            )
            density_params_complex = attrs.evolve(md_params_binder, restraintmask=complex_noh_restraint_mask)
            step_complex = MDRun(
                wnid=f"lower{i}_complex_{self.name}",
                mdin_template="md_restrained",
                mdparameters=density_params_complex,
                skippable=skippable,
            )
            md_nodes.append((step_binder, step_complex))

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
        bb_binder = MDRun(
            wnid=f"bb_binder_{self.name}",
            mdin_template="md_restrained",
            mdparameters=final_params,
            skippable=skippable,
        )
        bb_complex = MDRun(
            wnid=f"bb_complex_{self.name}",
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
            ntwx=ntwx_pdt,
            iwrap=iwrap,
            nscm=nscm,
        )
        free_binder = MDRun(
            wnid=f"free_binder_{self.name}",
            mdin_template="md",
            mdparameters=free_params,
            skippable=skippable,
        )
        if None in (complex_free_restraint_mask, complex_free_restraint_wt):
            mdin_template = "md"
        else:
            free_params = attrs.evolve(
                free_params, restraintmask=complex_free_restraint_mask, restraint_wt=complex_free_restraint_wt
            )
            mdin_template = "md_restrained"

        free_complex = MDRun(
            wnid=f"free_complex_{self.name}",
            mdin_template=mdin_template,
            mdparameters=free_params,
            skippable=skippable,
        )

        # Connect the workflow
        self.dag.add_edge(self.root, wnf_binder_top)
        self.dag.add_edge(self.root, wnf_binder_rst)
        self.dag.add_edge(self.root, wnf_binder_ref)
        self.dag.add_edge(self.root, wnf_complex_top)
        self.dag.add_edge(self.root, wnf_complex_rst)
        self.dag.add_edge(self.root, wnf_complex_ref)

        # Binder path
        self.dag.add_edge(wnf_binder_top, clash_fix_binder)
        self.dag.add_edge(wnf_binder_rst, clash_fix_binder)
        self.dag.add_edge(clash_fix_binder, min1_binder)
        self.dag.add_edge(wnf_binder_rst, crs_binder)
        self.dag.add_edge(min1_binder, heat_binder)
        self.dag.add_edge(heat_binder, density0_binder)
        self.dag.add_edge(density0_binder, crs_density0_binder)
        self.dag.add_edge(density0_binder, density1_binder)
        self.dag.add_edge(crs_density0_binder, density1_binder)

        # Restraints relaxation steps may vary
        previous_binder_step = density1_binder
        for step_binder, _ in md_nodes:
            self.dag.add_edge(previous_binder_step, step_binder)
            previous_binder_step = step_binder
        self.dag.add_edge(previous_binder_step, bb_binder)
        self.dag.add_edge(bb_binder, free_binder)

        # Complex path
        self.dag.add_edge(wnf_complex_top, clash_fix_complex)
        self.dag.add_edge(wnf_complex_rst, clash_fix_complex)
        self.dag.add_edge(clash_fix_complex, min1_complex)
        self.dag.add_edge(wnf_complex_rst, crs_complex)
        self.dag.add_edge(min1_complex, heat_complex)
        self.dag.add_edge(heat_complex, density0_complex)
        self.dag.add_edge(density0_complex, crs_density0_complex)
        self.dag.add_edge(density0_complex, density1_complex)
        self.dag.add_edge(crs_density0_complex, density1_complex)

        # Restraints relaxation steps may vary
        previous_complex_step = density1_complex
        for _, step_complex in md_nodes:
            self.dag.add_edge(previous_complex_step, step_complex)
            previous_complex_step = step_complex
        self.dag.add_edge(previous_complex_step, bb_complex)
        self.dag.add_edge(bb_complex, free_complex)

        # Connect to leaf
        self.dag.add_edge(crs_complex, self.leaf)
        self.dag.add_edge(crs_binder, self.leaf)
        self.dag.add_edge(free_binder, wnf_binder_ref_density0)
        self.dag.add_edge(free_complex, wnf_complex_ref_density0)
        self.dag.add_edge(wnf_binder_ref_density0, self.leaf)
        self.dag.add_edge(wnf_complex_ref_density0, self.leaf)
