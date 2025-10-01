import sys
from typing import Iterator, overload, Union
from collections import defaultdict

import MDAnalysis as mda

from amberflow.artifacts import BaseArtifactFile, fileartifact, BaseArtifact
from amberflow.primitives import filepath_t

__all__ = (
    "PythonScript",
    "BaseCSVFile",
    "AnalysisCSVFile",
    "BaseJSONFile",
    "AnalysisJSONFile",
    "BaseAmberMaskString",
    "AmberMaskString",
    "BaseRestraintMask",
    "CartesianRestraintMask",
    "RMSDRestraintMask1",
    "RMSDRestraintMask2",
    "BaseAmberAFEMask",
    "AmberTI1Mask",
    "AmberTI2Mask",
    "AmberSC1Mask",
    "AmberSC2Mask",
    "BaseAtomList",
    "CC1Atomlist",
    "CC2Atomlist",
    "SC1Atomlist",
    "SC2Atomlist",
)


@fileartifact
class PythonScript(BaseArtifactFile):
    prefix: str = ""
    suffix: str = ".py"
    tags: tuple[str] = ("",)

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, **kwargs)


class BaseCSVFile(BaseArtifactFile):
    pass


@fileartifact
class AnalysisCSVFile(BaseCSVFile):
    prefix: str = "fe_data"
    suffix: str = ".csv"
    tags: tuple[str] = ("",)

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, **kwargs)


class BaseJSONFile(BaseArtifactFile):
    pass


@fileartifact
class AnalysisJSONFile(BaseJSONFile):
    prefix: str = "analysis_record"
    suffix: str = ".json"
    tags: tuple[str] = ("",)

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, *args, prefix=self.prefix, suffix=self.suffix, **kwargs)


class BaseAmberMaskString(BaseArtifact):
    def __init__(self, data: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.data = str(data)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)

    def __hash__(self):
        return hash(self.data)

    def __getnewargs__(self):
        return (self.data[:],)

    def __eq__(self, string):
        if isinstance(string, BaseAmberMaskString):
            return self.data == string.data
        return self.data == string

    def __lt__(self, string):
        if isinstance(string, BaseAmberMaskString):
            return self.data < string.data
        return self.data < string

    def __le__(self, string):
        if isinstance(string, BaseAmberMaskString):
            return self.data <= string.data
        return self.data <= string

    def __gt__(self, string):
        if isinstance(string, BaseAmberMaskString):
            return self.data > string.data
        return self.data > string

    def __ge__(self, string):
        if isinstance(string, BaseAmberMaskString):
            return self.data >= string.data
        return self.data >= string

    def __contains__(self, char):
        if isinstance(char, BaseAmberMaskString):
            char = char.data
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __add__(self, other):
        if isinstance(other, BaseAmberMaskString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, str):
            return self.__class__(self.data + other)
        return self.__class__(self.data + str(other))

    def __radd__(self, other):
        if isinstance(other, str):
            return self.__class__(other + self.data)
        return self.__class__(str(other) + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    def __rmod__(self, template):
        return self.__class__(str(template) % self)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def casefold(self):
        return self.__class__(self.data.casefold())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        if isinstance(sub, BaseAmberMaskString):
            sub = sub.data
        return self.data.count(sub, start, end)

    def removeprefix(self, prefix, /):
        if isinstance(prefix, BaseAmberMaskString):
            prefix = prefix.data
        return self.__class__(self.data.removeprefix(prefix))

    def removesuffix(self, suffix, /):
        if isinstance(suffix, BaseAmberMaskString):
            suffix = suffix.data
        return self.__class__(self.data.removesuffix(suffix))

    def encode(self, encoding="utf-8", errors="strict"):
        encoding = "utf-8" if encoding is None else encoding
        errors = "strict" if errors is None else errors
        return self.data.encode(encoding, errors)

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        if isinstance(sub, BaseAmberMaskString):
            sub = sub.data
        return self.data.find(sub, start, end)

    def format(self, /, *args, **kwds):
        return self.data.format(*args, **kwds)

    def format_map(self, mapping):
        return self.data.format_map(mapping)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isascii(self):
        return self.data.isascii()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def isidentifier(self):
        return self.data.isidentifier()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isprintable(self):
        return self.data.isprintable()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    maketrans = str.maketrans

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        if isinstance(old, BaseAmberMaskString):
            old = old.data
        if isinstance(new, BaseAmberMaskString):
            new = new.data
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        if isinstance(sub, BaseAmberMaskString):
            sub = sub.data
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=False):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class AmberMaskString(BaseAmberMaskString):
    """
    default class for any mask
    """

    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class BaseRestraintMask(BaseAmberMaskString):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class CartesianRestraintMask(BaseRestraintMask):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class RMSDRestraintMask1(BaseRestraintMask):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class RMSDRestraintMask2(BaseRestraintMask):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class BaseAmberAFEMask(BaseAmberMaskString):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class AmberTI1Mask(BaseAmberAFEMask):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class AmberTI2Mask(BaseAmberAFEMask):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class AmberSC1Mask(BaseAmberAFEMask):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class AmberSC2Mask(BaseAmberAFEMask):
    def __init__(self, data, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)


class BaseAtomList(BaseArtifact):
    """A container to hold and iterate over properties of a list of atoms."""

    def __init__(
        self,
        names: list[str],
        ids: list[int],
        resnames: list[str],
        resids: list[int],
        chainids: list[str],
    ):
        # Basic validation to ensure all lists have the same length
        lengths = {len(names), len(ids), len(resnames), len(resids), len(chainids)}
        if len(lengths) > 1:
            raise ValueError("All attribute lists must have the same length.")

        self.names = names
        self.ids = ids
        self.resnames = resnames
        self.resids = resids
        self.chainids = chainids

    @classmethod
    def _from_mda_atoms(cls, atom_group: mda.AtomGroup) -> "BaseAtomList":
        """Factory method to create an BaseAtomList from an MDAnalysis.AtomGroup."""
        names: list[str] = []
        ids: list[int] = []
        resnames: list[str] = []
        resids: list[int] = []
        chainids: list[str] = []

        for atom in atom_group:
            names.append(atom.name)
            ids.append(atom.id)
            resnames.append(atom.resname)
            resids.append(atom.resid)
            # chainID may be missing
            chainids.append(getattr(atom, "chainID", ""))

        return cls(names, ids, resnames, resids, chainids)

    def mda_sel(self, hydrogens: bool = True) -> str:
        not_hydrogens = "" if hydrogens else " and not type H"
        res_to_atm = defaultdict(list)
        if hydrogens:
            for name, resname in zip(self.names, self.resnames):
                res_to_atm[resname].append(name)
        else:
            for name, resname in zip(self.names, self.resnames):
                if not name.startswith("H"):
                    res_to_atm[resname].append(name)
        res_sele = []
        for resname, atom_names in res_to_atm.items():
            atoms = " or ".join([f"name {atom}" for atom in atom_names])
            res_sele.append(f"(resname {resname} and ({atoms})){not_hydrogens}")
        full_sele = " or ".join(res_sele)
        return full_sele

    @overload
    def __getitem__(self, key: int) -> tuple[str, int, str, int, str]: ...

    @overload
    def __getitem__(self, key: slice) -> "BaseAtomList": ...

    def __getitem__(self, key: Union[int, slice]) -> Union["BaseAtomList", tuple[str, int, str, int, str]]:
        if isinstance(key, int):
            # Handle negative indices correctly
            if key < 0:
                key += len(self)
            if not 0 <= key < len(self):
                raise IndexError("AtomList index out of range")
            return (
                self.names[key],
                self.ids[key],
                self.resnames[key],
                self.resids[key],
                self.chainids[key],
            )
        elif isinstance(key, slice):
            return self.__class__(
                names=self.names[key],
                ids=self.ids[key],
                resnames=self.resnames[key],
                resids=self.resids[key],
                chainids=self.chainids[key],
            )
        else:
            raise TypeError(f"AtomList indices must be integers or slices, not {type(key).__name__}")

    def __len__(self) -> int:
        return len(self.names)

    def __iter__(self) -> Iterator[tuple[str, int, str, int, str]]:
        return zip(self.names, self.ids, self.resnames, self.resids, self.chainids)

    def __repr__(self) -> str:
        """Provide an unambiguous, reproducible representation of the AtomList."""
        # This format ensures that eval(repr(obj)) would recreate the object.
        return (
            f"{self.__class__.__name__}(\n"
            f"    names={self.names!r},\n"
            f"    ids={self.ids!r},\n"
            f"    resnames={self.resnames!r},\n"
            f"    resids={self.resids!r},\n"
            f"    chainids={self.chainids!r}\n"
            f")"
        )


class CC1Atomlist(BaseAtomList):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @classmethod
    def from_mda_atoms(cls, atom_group: mda.AtomGroup) -> "CC1Atomlist":
        return cls._from_mda_atoms(atom_group)


class CC2Atomlist(BaseAtomList):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @classmethod
    def from_mda_atoms(cls, atom_group: mda.AtomGroup) -> "CC2Atomlist":
        return cls._from_mda_atoms(atom_group)


class SC1Atomlist(BaseAtomList):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @classmethod
    def from_mda_atoms(cls, atom_group: mda.AtomGroup) -> "SC1Atomlist":
        return cls._from_mda_atoms(atom_group)


class SC2Atomlist(BaseAtomList):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @classmethod
    def from_mda_atoms(cls, atom_group: mda.AtomGroup) -> "SC2Atomlist":
        return cls._from_mda_atoms(atom_group)
