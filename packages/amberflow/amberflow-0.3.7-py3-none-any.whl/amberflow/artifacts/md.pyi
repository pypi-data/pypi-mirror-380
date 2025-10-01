from typing import List, Type, Any, Literal, Optional
from pathlib import Path

import MDAnalysis as mda

from amberflow.primitives import filepath_t, dirpath_t
from amberflow.artifacts import BaseArtifactFile, BaseArtifact

__all__ = (
    "BaseNMRRestraints",
    "AmberNMRRestraints",
    "BoreschRestraints",
    "CpptrajData",
    "Groupfile",
    "LambdaScheduleFile",
    "Remlog",
    "BaseMdoutMD",
    "TargetProteinMdoutMD",
    "TargetNucleicMdoutMD",
    "BinderLigandMdoutMD",
    "ComplexProteinLigandMdoutMD",
    "ComplexNucleicLigandMdoutMD",
    "BasePeriodicBox",
    "BaseTargetPeriodicBox",
    "BaseBinderPeriodicBox",
    "BaseComplexPeriodicBox",
    "TargetNucleicPeriodicBox",
    "TargetProteinPeriodicBox",
    "BinderLigandPeriodicBox",
    "ComplexProteinLigandPeriodicBox",
    "ComplexNucleicLigandPeriodicBox",
)

class BaseNMRRestraints(BaseArtifactFile):
    def __init__(
        self,
        filepath: filepath_t,
        *args: Any,
        prefix: str,
        suffix: str,
        **kwargs: Any,
    ) -> None: ...
    @staticmethod
    def get_restraint_str(
        indices: tuple[int, ...], r1: float, r2: float, r3: float, r4: float, rk2: float, rk3: float
    ) -> str: ...
    @classmethod
    def _write_amber_disang(
        cls,
        filepath: Path,
        *,
        indices_list: list[tuple[int, ...]],
        dists_or_angles: list[float],
        restraint_type: Literal["harmonic", "halfharmonic"],
        restraint_strength: float,
    ) -> None: ...
    @classmethod
    def _write_disang_from_mda_atoms(
        cls,
        filepath: Path,
        *,
        restraint_data: list[tuple[mda.core.groups.Atom, ..., float]],
        restraint_type: Literal["harmonic", "halfharmonic"] = "harmonic",
        restraint_strength: float = 5.0,
    ) -> None: ...
    @classmethod
    def _write_disang_from_indices(
        cls,
        filepath: Path,
        *,
        indices_list: list[tuple[int, ...]],
        dists_or_angles: list[float],
        restraint_type: Literal["harmonic", "halfharmonic"] = "harmonic",
        restraint_strength: float = 5.0,
    ) -> None: ...

class AmberNMRRestraints(BaseNMRRestraints):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(
        self,
        filepath: filepath_t,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def write_disang_from_mda_atoms(
        cls,
        dirpath: dirpath_t,
        *,
        restraint_data: list[tuple[mda.core.groups.Atom, ..., float]],
        restraint_type: Literal["harmonic", "halfharmonic"] = "harmonic",
        restraint_strength: float = 5.0,
    ) -> "AmberNMRRestraints": ...
    @classmethod
    def write_disang_from_indices(
        cls,
        dirpath: dirpath_t,
        *,
        indices_list: list[tuple[int, ...]],
        dists_or_angles: list[float],
        restraint_type: Literal["harmonic", "halfharmonic"] = "harmonic",
        restraint_strength: float = 5.0,
    ) -> "AmberNMRRestraints": ...

class BoreschRestraints(BaseNMRRestraints):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(
        self,
        filepath: filepath_t,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...

class CpptrajData(BaseArtifactFile):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(self, filepath: filepath_t, *args: Any, **kwargs: Any) -> None: ...

class Groupfile(BaseArtifactFile):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(self, filepath: filepath_t, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def from_lines(cls: Type["Groupfile"], filepath: filepath_t, lines: List[str]) -> "Groupfile": ...

class LambdaScheduleFile(BaseArtifact):
    prefix: str
    suffix: str
    tags: tuple[str]

    filepath: Optional[Path]
    lambda_type: Optional[str]
    function_type: Optional[str]
    match_type: Optional[str]
    parameter1: Optional[float]
    parameter2: Optional[float]

    def __init__(
        self,
        filepath: Optional[Path] = None,
        lambda_type: Optional[str] = None,
        function_type: Optional[str] = None,
        match_type: Optional[str] = None,
        parameter1: Optional[float] = None,
        parameter2: Optional[float] = None,
    ) -> None: ...
    @classmethod
    def from_file(cls, filepath: filepath_t) -> "LambdaScheduleFile": ...
    def write(self, filepath: Optional[filepath_t] = None) -> None: ...

class Remlog(BaseArtifactFile):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None: ...

class BaseMdoutMD(BaseArtifactFile):
    def __init__(self, filepath: filepath_t, *args: Any, check: bool = True, **kwargs: Any) -> None: ...
    @staticmethod
    def check_mdout(mdout: filepath_t) -> None: ...

class TargetProteinMdoutMD(BaseMdoutMD):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(self, filepath: filepath_t, *args: Any, check: bool = True, **kwargs: Any) -> None: ...

class TargetNucleicMdoutMD(BaseMdoutMD):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(self, filepath: filepath_t, *args: Any, check: bool = True, **kwargs: Any) -> None: ...

class BinderLigandMdoutMD(BaseMdoutMD):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(self, filepath: filepath_t, *args: Any, check: bool = True, **kwargs: Any) -> None: ...

class ComplexProteinLigandMdoutMD(BaseMdoutMD):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(self, filepath: filepath_t, *args: Any, check: bool = True, **kwargs: Any) -> None: ...

class ComplexNucleicLigandMdoutMD(BaseMdoutMD):
    prefix: str
    suffix: str
    tags: tuple[str]

    def __init__(self, filepath: filepath_t, *args: Any, check: bool = True, **kwargs: Any) -> None: ...

class BaseTargetPeriodicBox(BasePeriodicBox):
    pass

class BaseBinderPeriodicBox(BasePeriodicBox):
    pass

class BaseComplexPeriodicBox(BasePeriodicBox):
    pass

class BasePeriodicBox(BaseArtifact):
    truncated_octahedron_angle: float = 109.4712190
    def __init__(self, box: list[float]) -> None: ...

class TargetProteinPeriodicBox(BaseTargetPeriodicBox):
    def __init__(self, box: list[float]) -> None: ...

class TargetNucleicPeriodicBox(BaseTargetPeriodicBox):
    def __init__(self, box: list[float]) -> None: ...

class BinderLigandPeriodicBox(BaseBinderPeriodicBox):
    def __init__(self, box: list[float]) -> None: ...

class ComplexProteinLigandPeriodicBox(BaseComplexPeriodicBox):
    def __init__(self, box: list[float]) -> None: ...

class ComplexNucleicLigandPeriodicBox(BaseComplexPeriodicBox):
    def __init__(self, box: list[float]) -> None: ...
