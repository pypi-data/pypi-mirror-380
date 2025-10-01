import math
from pathlib import Path
from typing import Iterator, Literal, Optional, Union

import MDAnalysis as mda

from amberflow.artifacts import fileartifact, BaseArtifactFile, BaseArtifact, copyto, changebasedir
from amberflow.primitives import filepath_t, find_word_and_get_line, BadMDout, dirpath_t

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
        *args,
        prefix: str,
        suffix: str,
        **kwargs,
    ) -> None:
        super().__init__(filepath, *args, prefix=prefix, suffix=suffix, **kwargs)

    @staticmethod
    def get_restraint_str(
        indices: tuple[int, ...], r1: float, r2: float, r3: float, r4: float, rk2: float, rk3: float
    ) -> str:
        iat_str = ", ".join(map(str, indices))
        # Format the restraint entry
        restraint_str = (
            f"&rst iat={iat_str}\n r1={r1:.5f}, r2={r2:.5f}, r3={r3:.5f}, r4={r4:.3f}, rk2={rk2:.2f}, rk3={rk3:.2f} /\n"
        )
        return restraint_str

    @classmethod
    def _write_amber_disang(
        cls,
        filepath: Path,
        *,
        indices_list: list[tuple[int, ...]],
        dists_or_angles: list[float],
        restraint_type: Literal["harmonic", "halfharmonic"],
        restraint_strength: float,
    ) -> None:
        lines = []
        for indices, value in zip(indices_list, dists_or_angles):
            num_atoms = len(indices)
            if num_atoms == 2:
                r1, r4 = 0.0, 999.0
            elif num_atoms in [3, 4]:
                r1, r4 = -180.0, 180.0
            else:
                raise ValueError(f"Invalid number of atoms for restraint: {num_atoms}. Must be 2, 3, or 4.")
            # noinspection PyUnreachableCode
            if restraint_type == "harmonic":
                rk2 = rk3 = restraint_strength
            elif restraint_type == "halfharmonic":
                rk2 = 0.0
                rk3 = restraint_strength
            else:
                raise ValueError(f"Invalid restraint_type: '{restraint_type}'. Must be 'harmonic' or 'halfharmonic'.")

            # The target value for the restraint
            r2 = r3 = value
            lines.append(cls.get_restraint_str(indices, r1, r2, r3, r4, rk2, rk3))

        with open(filepath, "w") as f:
            f.writelines(lines)

    @classmethod
    def _write_disang_from_mda_atoms(
        cls,
        filepath: Path,
        *,
        restraint_data: list[tuple[mda.core.groups.Atom, ..., float]],
        restraint_type: Literal["harmonic", "halfharmonic"] = "harmonic",
        restraint_strength: float = 5.0,
    ) -> None:
        """
        Builds a restraint file from a list of tuples containing MDAnalysis atoms and a target value.
        """
        indices_list = []
        dists_or_angles = []

        for item in restraint_data:
            atoms = item[:-1]
            value = item[-1]
            if not all(isinstance(a, mda.core.groups.Atom) for a in atoms):
                raise TypeError("All items in the tuple except the last must be MDAnalysis.Atom objects.")

            # Atom IDs in MDAnalysis are 1-based, matching Amber's iat format.
            indices_list.append(tuple(atom.id for atom in atoms))
            dists_or_angles.append(value)

        cls._write_amber_disang(
            filepath,
            indices_list=indices_list,
            dists_or_angles=dists_or_angles,
            restraint_type=restraint_type,
            restraint_strength=restraint_strength,
        )

    @classmethod
    def _write_disang_from_indices(
        cls,
        filepath: Path,
        *,
        indices_list: list[tuple[int, ...]],
        dists_or_angles: list[float],
        restraint_type: Literal["harmonic", "halfharmonic"] = "harmonic",
        restraint_strength: float = 5.0,
    ) -> None:
        """
        Builds a restraint file from lists of atom indices and target values.
        """
        if len(indices_list) != len(dists_or_angles):
            raise ValueError("indices_list and dists_or_angles must have the same length.")

        cls._write_amber_disang(
            filepath,
            indices_list=indices_list,
            dists_or_angles=dists_or_angles,
            restraint_type=restraint_type,
            restraint_strength=restraint_strength,
        )


@fileartifact
class AmberNMRRestraints(BaseNMRRestraints):
    prefix: str = "rest"
    suffix: str = ".disang"
    tags: tuple = tuple()

    def __init__(
        self,
        filepath: filepath_t,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, **kwargs)

    @classmethod
    def write_disang_from_mda_atoms(
        cls,
        dirpath: dirpath_t,
        *,
        restraint_data: list[tuple[mda.core.groups.Atom, ..., float]],
        restraint_type: Literal["harmonic", "halfharmonic"] = "harmonic",
        restraint_strength: float = 5.0,
    ) -> "AmberNMRRestraints":
        """
        Builds a restraint file from a list of tuples containing MDAnalysis atoms and a target value.
        """
        filepath = Path(dirpath, cls.prefix + cls.suffix)
        super()._write_disang_from_mda_atoms(
            filepath,
            restraint_data=restraint_data,
            restraint_type=restraint_type,
            restraint_strength=restraint_strength,
        )
        return cls(filepath)

    @classmethod
    def write_disang_from_indices(
        cls,
        dirpath: dirpath_t,
        *,
        indices_list: list[tuple[int, ...]],
        dists_or_angles: list[float],
        restraint_type: Literal["harmonic", "halfharmonic"] = "harmonic",
        restraint_strength: float = 5.0,
    ) -> "AmberNMRRestraints":
        filepath = Path(dirpath, cls.prefix + cls.suffix)
        super()._write_disang_from_indices(
            filepath,
            indices_list=indices_list,
            dists_or_angles=dists_or_angles,
            restraint_type=restraint_type,
            restraint_strength=restraint_strength,
        )
        return cls(filepath)


@fileartifact
class BoreschRestraints(BaseNMRRestraints):
    prefix: str = "rest"
    suffix: str = ".in"
    tags: tuple = ("alchemical",)

    def __init__(
        self,
        filepath: filepath_t,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, **kwargs)


@fileartifact
class CpptrajData(BaseArtifactFile):
    prefix: str = ""
    suffix: str = ".dat"
    tags: tuple[str] = ("cpptraj",)

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, **kwargs)


@fileartifact
class Groupfile(BaseArtifactFile):
    prefix: str = ""
    suffix: str = ".groupfile"
    tags: tuple[str] = ("",)

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, **kwargs)

    @classmethod
    def from_lines(cls, filepath: filepath_t, lines: list[str]) -> "Groupfile":
        """Create a Groupfile from a list of lines."""
        with open(filepath, "w") as f:
            f.write("\n".join(lines))
            f.write("\n")
        return cls(filepath)


# noinspection PyUnresolvedReferences
@copyto
@changebasedir
class LambdaScheduleFile(BaseArtifact):
    prefix: str = "lambda"
    suffix: str = ".sch"
    tags: tuple[str] = ("",)

    LAMBDA_TYPES: set[str] = {
        "TypeGen",
        "TypeBAT",
        "TypeRestBA",
        "TypeEleRec",
        "TypeEleCC",
        "TypeEleSC",
        "TypeVDW",
        "TypeRestB",
        "TypeRestA",
        "TypeNone",
    }
    FUNCTION_TYPES: set[str] = {
        "linear",
        "smooth_step0",
        "smooth_step1",
        "smooth_step2",
        "smooth_step3",
        "smooth_step4",
    }
    MATCH_TYPES: set[str] = {"complementary", "symmetric"}

    def __init__(
        self,
        filepath: Optional[Path] = None,
        lambda_type: Optional[str] = None,
        function_type: Optional[str] = None,
        match_type: Optional[str] = None,
        parameter1: Optional[float] = None,
        parameter2: Optional[float] = None,
    ) -> None:
        self.filepath = filepath if filepath is None else LambdaScheduleFile._from_filepath(filepath)
        self.lambda_type = lambda_type
        self.function_type = function_type
        self.match_type = match_type
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    @property
    def lambda_type(self) -> Optional[str]:
        return self._lambda_type

    @lambda_type.setter
    def lambda_type(self, value: Optional[str]):
        if value is not None and value not in self.LAMBDA_TYPES:
            raise ValueError(f"'{value}' is not a valid lambda_type.")
        self._lambda_type = value

    @property
    def function_type(self) -> Optional[str]:
        return self._function_type

    @function_type.setter
    def function_type(self, value: Optional[str]):
        if value is not None and value not in self.FUNCTION_TYPES:
            raise ValueError(f"'{value}' is not a valid `function_type`.")
        self._function_type = value

    @property
    def match_type(self) -> Optional[str]:
        return self._match_type

    @match_type.setter
    def match_type(self, value: Optional[str]):
        if value is not None and value not in self.MATCH_TYPES:
            raise ValueError(f"'{value}' is not a valid `match_type`.")
        self._match_type = value

    @property
    def parameter1(self) -> Optional[float]:
        return self._parameter1

    @parameter1.setter
    def parameter1(self, value: Optional[float]):
        if value is not None and not (0.0 <= value <= 1.0):
            raise ValueError(f"`parameter1` must be between 0.0 and 1.0, not {value}.")
        self._parameter1 = value

    @property
    def parameter2(self) -> Optional[float]:
        return self._parameter2

    @parameter2.setter
    def parameter2(self, value: Optional[float]):
        if value is not None and not (0.0 <= value <= 1.0):
            raise ValueError(f"`parameter2` must be between 0.0 and 1.0, not {value}.")
        self._parameter2 = value

    @classmethod
    def from_file(cls, filepath: filepath_t) -> "LambdaScheduleFile":
        """
        Creates a LambdaScheduleFile instance by reading and parsing a file.

        Args:
            filepath: The path to the schedule file to read.

        Returns:
            A new instance of LambdaScheduleFile with populated attributes.
        """
        filepath = LambdaScheduleFile._from_filepath(filepath)
        content = filepath.read_text().strip()
        parts = [p.strip() for p in content.split(",")]

        if len(parts) != 5:
            raise IOError(f"Expected 5 comma-separated values in {filepath}, but found {len(parts)}.")
        try:
            return cls(
                filepath=filepath,
                lambda_type=parts[0],
                function_type=parts[1],
                match_type=parts[2],
                parameter1=float(parts[3]),
                parameter2=float(parts[4]),
            )
        except ValueError as e:
            raise IOError(f"Error parsing values from {filepath}: {e}") from e

    def write(self, filepath: Optional[filepath_t] = None) -> None:
        """
        Writes the current schedule attributes to a file.

        Args:
            filepath: The path to write to. If None, uses the instance's filepath.
        """
        for attr in ["lambda_type", "function_type", "match_type", "parameter1", "parameter2"]:
            if getattr(self, attr) is None:
                raise ValueError(f"Attribute '{attr}' must be set before writing the file.")

        # Format the output string
        output_string = (
            f"{self.lambda_type}, {self.function_type}, {self.match_type}, {self.parameter1}, {self.parameter2}\n"
        )
        output_path = Path(filepath) if filepath else self.filepath
        with output_path.open(mode="a", encoding="utf-8") as f:
            f.write(output_string)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(filepath='{self.filepath}', lambda_type='{self.lambda_type}', "
            f"function_type='{self.function_type}', match_type='{self.match_type}', "
            f"parameter1={self.parameter1}, parameter2={self.parameter2})"
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(filepath={self.filepath})"

    def __fspath__(self) -> Union[str, bytes, Path]:
        return str(self.filepath)


@fileartifact
class Remlog(BaseArtifactFile):
    prefix: str = "remd"
    suffix: str = ".log"
    tags: tuple[str] = ("",)

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, **kwargs)


class BaseMdoutMD(BaseArtifactFile):
    def __init__(self, filepath: filepath_t, *args, check=True, **kwargs) -> None:
        super().__init__(filepath, *args, **kwargs)
        if check:
            BaseMdoutMD.check_mdout(filepath)

    @staticmethod
    def check_mdout(mdout: filepath_t) -> None:
        if not find_word_and_get_line(mdout, "Total wall time:"):
            raise BadMDout(f"Cannot find 'Total wall time' in {mdout}\nMDout file may be incomplete or corrupted.")


@fileartifact
class TargetProteinMdoutMD(BaseMdoutMD):
    prefix: str = "target"
    suffix: str = ".mdout"
    tags: tuple[str] = ("target", "protein")

    def __init__(self, filepath: filepath_t, *args, check=True, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, check=check, **kwargs)


@fileartifact
class TargetNucleicMdoutMD(BaseMdoutMD):
    prefix: str = "target"
    suffix: str = ".mdout"
    tags: tuple[str] = ("target", "nucleic")

    def __init__(self, filepath: filepath_t, *args, check=True, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, check=check, **kwargs)


@fileartifact
class BinderLigandMdoutMD(BaseMdoutMD):
    prefix: str = "binder"
    suffix: str = ".mdout"
    tags: tuple[str] = ("ligand",)

    def __init__(self, filepath: filepath_t, *args, check=True, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, check=check, **kwargs)


@fileartifact
class ComplexProteinLigandMdoutMD(BaseMdoutMD):
    prefix: str = "complex"
    suffix: str = ".mdout"
    tags: tuple[str] = ("protein", "ligand")

    def __init__(self, filepath: filepath_t, *args, check=True, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, check=check, **kwargs)


@fileartifact
class ComplexNucleicLigandMdoutMD(BaseMdoutMD):
    prefix: str = "complex"
    suffix: str = ".mdout"
    tags: tuple[str] = ("nucleic", "ligand")

    def __init__(self, filepath: filepath_t, *args, check=True, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, check=check, **kwargs)


class BasePeriodicBox(BaseArtifact):
    """
    Represents a periodic box with dimensions and angles.
    """

    truncated_octahedron_angle: float = 109.4712190

    def __init__(self, box: list[float]) -> None:
        if len(box) != 6:
            raise ValueError("Box must have exactly 6 elements: [a, b, c, alpha, beta, gamma]")
        self.a = box[0]
        self.b = box[1]
        self.c = box[2]
        if math.isclose(box[3], BasePeriodicBox.truncated_octahedron_angle, abs_tol=0.1):
            # Truncated octahedron box. Replace with precise dimensions, just in case:
            self.alpha = BasePeriodicBox.truncated_octahedron_angle
            self.beta = BasePeriodicBox.truncated_octahedron_angle
            self.gamma = BasePeriodicBox.truncated_octahedron_angle
        else:
            self.alpha = box[3]
            self.beta = box[4]
            self.gamma = box[5]

    def __str__(self) -> str:
        return f"-X {self.a} -Y {self.b} -Z {self.c} -al {self.alpha} -bt {self.beta} -gm {self.gamma}"

    def __repr__(self) -> str:
        box_list = [self.a, self.b, self.c, self.alpha, self.beta, self.gamma]
        return f"PeriodicBox(box={box_list})"

    def __iter__(self) -> Iterator[float]:
        return iter([self.a, self.b, self.c, self.alpha, self.beta, self.gamma])

    # noinspection PyUnusedLocal
    @classmethod
    def from_filepath(cls, filepath: filepath_t, *args, **kwargs) -> "BasePeriodicBox":
        filepath: Path = cls._from_filepath(filepath)
        with open(filepath, "r") as f:
            line = f.readline().strip()
            box_values = [float(x) for x in line.split()]
            if len(box_values) != 6:
                raise ValueError(f"Box file {filepath} must contain exactly 6 float values.")

            obj = cls(box_values)
            setattr(obj, "filepath", filepath)
            return obj


class BaseTargetPeriodicBox(BasePeriodicBox):
    pass


class BaseBinderPeriodicBox(BasePeriodicBox):
    pass


class BaseComplexPeriodicBox(BasePeriodicBox):
    pass


class TargetProteinPeriodicBox(BaseTargetPeriodicBox):
    prefix: str = "target"
    suffix: str = ".box"
    tags: tuple[str] = ("protein",)

    def __init__(self, box: list[float]) -> None:
        super().__init__(box)


class TargetNucleicPeriodicBox(BaseTargetPeriodicBox):
    prefix: str = "target"
    suffix: str = ".box"
    tags: tuple[str] = ("nucleic",)

    def __init__(self, box: list[float]) -> None:
        super().__init__(box)


class BinderLigandPeriodicBox(BaseBinderPeriodicBox):
    prefix: str = "binder"
    suffix: str = ".box"
    tags: tuple[str] = ("ligand",)

    def __init__(self, box: list[float]) -> None:
        super().__init__(box)


class ComplexProteinLigandPeriodicBox(BaseComplexPeriodicBox):
    prefix: str = "complex"
    suffix: str = ".box"
    tags: tuple[str] = ("protein", "ligand")

    def __init__(self, box: list[float]) -> None:
        super().__init__(box)


class ComplexNucleicLigandPeriodicBox(BaseComplexPeriodicBox):
    prefix: str = "complex"
    suffix: str = ".box"
    tags: tuple[str] = ("nucleic", "ligand")

    def __init__(self, box: list[float]) -> None:
        super().__init__(box)
