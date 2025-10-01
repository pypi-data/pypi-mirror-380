from amberflow.artifacts import BaseParameterModFile, BaseLibFile, BaseFrcmodFile
from amberflow.artifacts import (
    BaseStructureFile,
    fileartifact,
    BaseParameterFile,
    BaseComplexTopologyFile,
    BaseComplexStructureFile,
    BaseBinderStructureFile,
    BaseTargetStructureFile,
)
from amberflow.primitives import filepath_t

__all = (
    "BaseDockStructureFile",
    "BaseDockComplexTopologyFile",
    "BaseDockTargetStructureFile",
    "BaseDockBinderStructureFile",
    "BaseDockComplexStructureFile",
    "DockProteinTarget",
    "DockTemplate",
    "DockBinderLib",
    "DockBinderFrcmod",
    "DockBinderModFrcmod",
    "DockProteinTargetModFrcmod",
)


class BaseDockStructureFile(BaseStructureFile):
    pass


class BaseDockTopologyFile(BaseComplexTopologyFile):
    pass


class BaseDockComplexTopologyFile(BaseDockTopologyFile):
    pass


class BaseDockTargetStructureFile(BaseTargetStructureFile):
    pass


class BaseDockBinderStructureFile(BaseBinderStructureFile):
    pass


class BaseDockComplexStructureFile(BaseComplexStructureFile):
    pass


class BaseDockParameterFile(BaseParameterFile):
    pass


class BaseDockParameterModFile(BaseParameterModFile):
    pass


class BaseDockLibFile(BaseDockParameterFile):
    pass


class BaseDockFrcmodFile(BaseDockParameterModFile):
    pass


class BaseBoxFile(BaseStructureFile):
    pass


class BaseBoxTargetFile(BaseBoxFile):
    pass


class BaseBoxBinderFile(BaseBoxFile):
    pass


class BaseBoxComplexFile(BaseBoxFile):
    pass


@fileartifact
class DockProteinTarget(BaseDockTargetStructureFile):
    prefix: str = "docktarget"
    suffix: str = ".pdb"
    tags: tuple = ("protein",)

    def __init__(self, filepath: filepath_t) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix)


@fileartifact
class DockBinderLigand(BaseDockBinderStructureFile):
    prefix: str = "dockbinder"
    suffix: str = ".pdb"
    tags: tuple = ("ligand",)

    def __init__(self, filepath: filepath_t) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix)


@fileartifact
class DockProteinLigandComplexPDB(BaseDockComplexStructureFile):
    prefix: str = "dockcomplex"
    suffix: str = ".pdb"
    tags: tuple = ("protein", "ligand")

    def __init__(self, filepath: filepath_t) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix)


@fileartifact
class DockProteinLigandComplexRestart(BaseDockComplexStructureFile):
    prefix: str = "dockbinder"
    suffix: str = ".rst7"
    tags: tuple = ("protein", "ligand")

    def __init__(self, filepath: filepath_t) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix)


@fileartifact
class DockProteinLigandComplexTopology(BaseDockComplexTopologyFile):
    prefix: str = "dockcomplex"
    suffix: str = ".parm7"
    tags: tuple = ("protein", "ligand")

    def __init__(self, filepath: filepath_t) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix)


@fileartifact
class DockBinderLib(BaseLibFile):
    prefix: str = "dockbinder"
    suffix: str = ".lib"
    tags: tuple = tuple()

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix, *args, **kwargs)


@fileartifact
class DockBinderFrcmod(BaseFrcmodFile):
    prefix: str = "dockbinder"
    suffix: str = ".frcmod"
    tags: tuple = tuple()

    def __init__(self, filepath: filepath_t, *, priority: int = 10) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix, priority=priority)


@fileartifact
class BoxBinderLigandPDB(BaseBoxBinderFile):
    prefix: str = "boxbinder"
    suffix: str = ".pdb"
    tags: tuple[str] = ("ligand",)

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix, **kwargs)


@fileartifact
class BoxComplexProteinLigandPDB(BaseBoxComplexFile):
    prefix: str = "boxcomplex"
    suffix: str = ".pdb"
    tags: tuple[str] = (
        "protein",
        "ligand",
    )

    def __init__(self, filepath: filepath_t, *args, **kwargs) -> None:
        super().__init__(filepath, prefix=self.prefix, suffix=self.suffix, **kwargs)
