from typing import Optional

import attrs

from amberflow.artifacts import (
    BaseComplexStructureFile,
    BaseBinderTopologyFile,
    BaseBinderStructureFile,
    BaseBinderStructureReferenceFile,
    BaseComplexTopologyFile,
    BaseComplexStructureReferenceFile,
)
from amberflow.flows import BaseFlow
from amberflow.worknodes import (
    Filter,
    MDRun,
    MinRestrainedParameters,
    HeatingParameters,
    MDParameters,
    GetBoresch,
)

__all__ = ("FlowBoxRelax1",)


class FlowBoxRelax1(BaseFlow):
    def __init__(
        self,
        name: str = "FlowBoxRelax1",
        *,
        complex_full_restraint_mask: str,
        complex_noh_restraint_mask: str,
        binder_full_restraint_mask: str,
        binder_noh_restraint_mask: str,
        strong_restraint_wt: int = 50,
        complex_free_restraint_mask: Optional[str] = None,
        complex_free_restraint_wt: Optional[int] = None,
        nstlim_free_complex: int = 1000000,
        nstlim_free_binder: int = 250000,
        nstlim_heat: int = 100000,
        ntpr_free: int = 1000,
        maxcyc: int = 1000,
        ncyc: int = 100,
        iwrap: int = 0,
        nscm: int = 0,
        skippable: bool = True,
    ):
        super().__init__(name)
        # Set all parameters as attributes
        for name, value in locals().items():
            if name != "self":
                setattr(self, name, value)

        ########## Filters ##########
        wnf_binderinputs = Filter(
            f"wnf_binderinputs_{self.name}",
            artifact_types=(
                BaseBinderTopologyFile,
                BaseBinderStructureFile,
                BaseBinderStructureReferenceFile,
            ),
            fail_if_no_artifacts=True,
            single=True,
        )
        wnf_complexinputs = Filter(
            f"wnf_complexinputs{self.name}",
            artifact_types=(
                BaseComplexTopologyFile,
                BaseComplexStructureFile,
                BaseComplexStructureReferenceFile,
            ),
            fail_if_no_artifacts=True,
            single=True,
        )

        ########## Minimization ##########
        min_params_binder = MinRestrainedParameters(
            ncyc=50, maxcyc=200, restraintmask=binder_full_restraint_mask, restraint_wt=strong_restraint_wt
        )
        min_binder = MDRun(
            wnid=f"min_binder_{self.name}",
            mdin_template="min_restrained",
            mdparameters=min_params_binder,
            engine="pmemd.cuda",
            skippable=skippable,
        )
        min_params_complex = attrs.evolve(min_params_binder, restraintmask=complex_full_restraint_mask)
        min_complex = MDRun(
            wnid=f"min_complex_{self.name}",
            mdin_template="min_restrained",
            mdparameters=min_params_complex,
            engine="pmemd",
            skippable=skippable,
        )

        ########## Heating ##########
        binder_heat_params = HeatingParameters(
            nstlim=nstlim_heat,
            tempi=100,
            temp0=298,
            gamma_ln=2.0,
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

        ########## 'Free' MD ##########
        free_binder_params = MDParameters(
            nstlim=nstlim_free_binder,
            ntpr=ntpr_free,
            dt=0.004,
            gamma_ln=5.0,
            ntwx=250,
            iwrap=iwrap,
            nscm=nscm,
        )
        free_binder = MDRun(
            wnid=f"free_binder_{self.name}",
            mdin_template="md",
            mdparameters=free_binder_params,
            skippable=skippable,
        )
        if None in (complex_free_restraint_mask, complex_free_restraint_wt):
            free_complex_params = attrs.evolve(free_binder_params, nstlim=nstlim_free_complex)
            mdin_template = "md"
        else:
            free_complex_params = attrs.evolve(
                free_binder_params,
                nstlim=nstlim_free_complex,
                restraintmask=complex_free_restraint_mask,
                restraint_wt=complex_free_restraint_wt,
            )
            mdin_template = "md_restrained"

        free_complex = MDRun(
            wnid=f"free_complex_{self.name}",
            mdin_template=mdin_template,
            mdparameters=free_complex_params,
            skippable=skippable,
        )
        boresch = GetBoresch(wnid="boresch", skippable=True)

        ########## edges ##########
        self.dag.add_edge(self.root, wnf_binderinputs)
        self.dag.add_edge(self.root, wnf_complexinputs)

        self.dag.add_edge(wnf_binderinputs, min_binder)
        self.dag.add_edge(wnf_complexinputs, min_complex)

        self.dag.add_edge(min_binder, heat_binder)
        self.dag.add_edge(min_complex, heat_complex)

        self.dag.add_edge(heat_binder, free_binder)
        self.dag.add_edge(heat_complex, free_complex)
        self.dag.add_edge(free_complex, boresch)

        self.dag.add_edge(free_binder, self.leaf)
        self.dag.add_edge(free_complex, self.leaf)
        self.dag.add_edge(boresch, self.leaf)
