import shlex
from abc import ABC, abstractmethod
import os
from logging import Logger
import subprocess as sp
from pathlib import Path
from typing import Union, Optional, Sequence, Any, overload

from typing_extensions import override

from amberflow.primitives import dirpath_t, filepath_t, _run_command
from amberflow.execution import BaseDataMover, RsyncMover

__all__ = ("BaseExecutor", "LocalExecutor", "RemoteExecutor")


# noinspection PyUnresolvedReferences
class BaseExecutor(ABC):
    """An abstract base class for an immutable command execution context.

    This ABC provides a common interface for running commands in various
    environments, such as locally or on a remote server. It is designed to
    hold configuration details like base directories and server information.

    Instances are **immutable**. Use `replace()` to create a new instance with changes
    """

    __slots__ = ("initialized",)

    def __init__(self, *args, asynch: bool = False, **kwargs):
        super().__setattr__("asynch", asynch)
        super().__setattr__("initialized", False)

    def __setattr__(self, name: str, value: Any) -> None:
        if self.initialized:
            raise AttributeError(f"'{self.__class__.__name__}' instances are immutable.")
        return super().__setattr__(name, value)

    # Define custom serialization methods for pickling and unpickling, since __slots__ + immutability are being used
    def __getstate__(self) -> dict[str, Any]:
        state = {}
        for slot in self.__slots__:
            if hasattr(self, slot):
                state[slot] = getattr(self, slot)
        return state

    def __setstate__(self, state: dict[str, Any]) -> None:
        for key, value in state.items():
            super().__setattr__(key, value)
        object.__setattr__(self, "initialized", True)

    def __delattr__(self, name: str) -> None:
        raise AttributeError(f"'{self.__class__.__name__}' instances are immutable.")

    def replace(self, **changes: Any) -> "BaseExecutor":
        """
        Returns a new instance of the executor with specified attributes replaced.

        Args:
            **changes: Keyword arguments for the attributes to change.
                       Keywords must be valid attributes of the Executor.

        Returns:
            A new instance of the same class with the updated attributes.

        Raises:
            TypeError: If a keyword argument is not a valid attribute.
        """
        constructor_slots = [s for s in self.__slots__ if not s.startswith("_")]
        current_args = {slot: getattr(self, slot) for slot in constructor_slots if hasattr(self, slot)}

        for key, value in changes.items():
            if key not in current_args:
                raise TypeError(f"'{key}' is not a valid keyword argument for {self.__class__.__name__}")
            current_args[key] = value

        return self.__class__(**current_args)

    @abstractmethod
    def run(self, cmd: Union[list[str], str], logger: Logger, *, cwd: dirpath_t, **kwargs) -> sp.CompletedProcess:
        raise NotImplementedError

    def download(self, local_filepath: filepath_t, logger: Logger) -> Union[dirpath_t, filepath_t]:
        raise NotImplementedError(f"Downloading files is not implemented for executor {self.__class__.__name__}.")

    @staticmethod
    def validate(cwd: dirpath_t, expected: Sequence[filepath_t], logger: Logger):
        """A helper to check for file existence."""
        logger.debug(f"Validating expected files in local directory: {cwd}")
        for file_path in expected:
            full_path = Path(file_path)
            if not full_path.is_absolute():
                full_path = Path(cwd) / file_path

            if not full_path.exists():
                err_msg = f"Validation failed. Expected file '{full_path}' not found."
                logger.error(err_msg)
                raise FileNotFoundError(err_msg)
        logger.debug("All expected files found locally.")

    def _add_to_environment(self, add_to_env: Optional[dict[str, str]] = None) -> Any:
        """A helper to add values to the working environment."""
        raise NotImplementedError

    @staticmethod
    def run_command(
        command: str,
        logger: Logger,
        *,
        cwd: Optional[dirpath_t] = None,
        env: Optional[dict] = None,
        check: bool = True,
        timeout: Optional[int] = None,
    ) -> sp.CompletedProcess:
        return _run_command(command, logger, cwd=cwd, env=env, check=check, timeout=timeout)


class LocalExecutor(BaseExecutor):
    """Executes a command directly on the local machine."""

    asynch: bool
    __slots__ = BaseExecutor.__slots__ + ("asynch",)

    def __init__(self, asynch: bool = False):
        super().__init__(asynch=asynch)
        super().__setattr__("initialized", True)

    @override
    def run(
        self,
        cmd: Union[list[str], str],
        logger: Logger,
        *,
        cwd: dirpath_t,
        add_to_env: Optional[dict] = None,
        timeout: Optional[int] = None,
        **kwargs,
    ) -> sp.CompletedProcess:
        if not self.initialized:
            raise RuntimeError(
                f"{self.__class__.__name__} is not properly initialized. "
                "Ensure remote_server, remote_base_dir, and local_base_dir are set."
            )
        cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
        env = self._add_to_environment(add_to_env)
        logger.info(f"Running command locally in '{cwd}':\n{cmd_str}")
        return super().run_command(cmd_str, logger, cwd=cwd, check=True, env=env)

    @override
    def _add_to_environment(self, add_to_env: Optional[dict[str, str]] = None) -> Any:
        """A helper to add values to the working environment."""
        new_env = os.environ.copy()
        if add_to_env is not None:
            new_env.update(add_to_env)
        return new_env


class RemoteExecutor(BaseExecutor):
    """Executes a command on a remote server via SSH.

    This class provides a context for running commands on a remote machine.
    It manages the connection details and handles file synchronization (upload
    and download) between the local and remote working directories using rsync.

    Instances of this class are immutable.

    Parameters
    ----------
    remote_server : str, optional
        The address of the remote server (e.g., 'user@hostname').
    remote_base_dir : dirpath_t, optional
        The absolute path to the base working directory on the remote server.
    local_base_dir : dirpath_t, optional
        The absolute path to the base working directory on the local machine.
    data_mover : BaseDataMover
            An instance of a data mover (e.g., RsyncMover) for file synchronization.

    Attributes
    ----------
    remote_server : Optional[str]
        The address of the remote server.
    remote_base_dir : Optional[dirpath_t]
        The base working directory on the remote machine.
    local_base_dir : Optional[dirpath_t]
        The base working directory on the local machine for path mapping.
    keyfile : Optional[filepath_t]
        The key file for SSH authentication, if required.
    data_mover : BaseDataMover
            An instance of a data mover (e.g., RsyncMover) for file synchronization.
    initialized : bool
        True if the executor has all required parameters to run, otherwise False.
    """

    # I have to list the attributes so PyCharm doesn't complain
    remote_server: Optional[str]
    remote_base_dir: Optional[Path]
    local_base_dir: Optional[Path]
    keyfile: Optional[Path]
    data_mover: Optional[BaseDataMover]
    initialized: bool
    asynch: bool
    __slots__ = BaseExecutor.__slots__ + (
        "remote_server",
        "remote_base_dir",
        "local_base_dir",
        "keyfile",
        "data_mover",
        "asynch",
    )

    def __init__(
        self,
        remote_server: Optional[str] = None,
        remote_base_dir: Optional[dirpath_t] = None,
        local_base_dir: Optional[dirpath_t] = None,
        keyfile: Optional[filepath_t] = None,
        data_mover: Optional[BaseDataMover] = None,
        asynch: bool = False,
    ):
        super().__init__(asynch=asynch)
        super().__setattr__("remote_server", remote_server)
        super().__setattr__("remote_base_dir", None if remote_base_dir is None else Path(remote_base_dir))
        super().__setattr__("local_base_dir", None if local_base_dir is None else Path(local_base_dir))
        super().__setattr__("keyfile", None if keyfile is None else Path(keyfile))

        default_data_mover = None if remote_server is None else RsyncMover(remote_server, self.keyfile)
        super().__setattr__("data_mover", default_data_mover if data_mover is None else data_mover)

        # Ensure that the remote server and directories are set before marking as initialized
        if remote_server is None or remote_base_dir is None or local_base_dir is None:
            super().__setattr__("initialized", False)
        else:
            super().__setattr__("initialized", True)

    @override
    def run(
        self,
        cmd: Union[list[str], str],
        logger: Logger,
        *,
        cwd: dirpath_t,
        add_to_env: Optional[dict] = None,
        timeout: Optional[int] = None,
        check: bool = True,
        **kwargs,
    ) -> sp.CompletedProcess:
        if not self.initialized:
            raise RuntimeError(
                f"{self.__class__.__name__} is not properly initialized. "
                "Ensure remote_server, remote_base_dir, and local_base_dir are set."
            )
        exclude: Union[None, Sequence[str]] = kwargs.get("exclude")
        cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
        remote_cwd = Path(self.remote_base_dir) / Path(cwd).relative_to(self.local_base_dir)

        if kwargs.get("upload", True):
            logger.info(f"Creating remote directory: {self.remote_server}:{remote_cwd}")
            self.run_remote_command(
                f"mkdir -p {remote_cwd}", logger, cwd=self.local_base_dir, keyfile=self.keyfile, check=True
            )
            logger.info(f"Uploading files from {cwd} to {self.remote_server}:{remote_cwd}")
            # self.rsync(f"{cwd}/", f"{self.remote_server}:{remote_cwd}/", self.local_base_dir, logger, exclude=exclude)
            self.data_mover.upload(cwd, remote_cwd, logger, exclude=exclude)

        env_prefix = self._add_to_environment(add_to_env)

        # Prepend the environment variables to the command
        remote_command_to_run = f"cd {remote_cwd} && {env_prefix} {cmd_str}"
        if self.asynch:
            remote_command_to_run = f"nohup bash -c '{remote_command_to_run}' &> /dev/null &"

        logger.info(f"Running command remotely in '{remote_cwd}':\n{remote_command_to_run}")
        p = self.run_remote_command(
            remote_command_to_run, logger, cwd=self.local_base_dir, keyfile=self.keyfile, check=check, timeout=timeout
        )

        if kwargs.get("download", True):
            logger.info(f"Downloading results from {self.remote_server}:{remote_cwd} back to {cwd}")
            # self.rsync(f"{self.remote_server}:{remote_cwd}/", f"{cwd}/", self.local_base_dir, logger, exclude=exclude)
            self.data_mover.download(remote_cwd, cwd, logger, exclude=exclude)

        return p

    @override
    def _add_to_environment(self, add_to_env: Optional[dict[str, str]] = None) -> Any:
        """A helper to add values to the working environment."""
        env_prefix = ""
        if add_to_env:
            # Use shlex.quote to handle spaces and special characters safely
            parts = [f"{key}={shlex.quote(str(value))}" for key, value in add_to_env.items()]
            env_prefix = " ".join(parts)
        return env_prefix

    def run_remote_command(
        self,
        command: str,
        logger: Logger,
        *,
        cwd: dirpath_t,
        keyfile: Optional[filepath_t] = None,
        check: bool = True,
        timeout: Optional[int] = None,
    ) -> sp.CompletedProcess:
        if keyfile is None:
            cmd = f'ssh {self.remote_server} "{command}"'
        else:
            cmd = f'ssh -i {keyfile} {self.remote_server} "{command}"'
        if logger is not None:
            logger.debug(f"Running remote command:\n{cmd}")
        # Pass the timeout to the underlying run_command call
        return super().run_command(cmd, logger, cwd=cwd, check=check, timeout=timeout)

    def rsync(
        self, src: dirpath_t, dest: dirpath_t, cwd: dirpath_t, logger: Logger, exclude: Optional[Sequence[str]] = None
    ):
        cmd_list = ["rsync", "-avzu", "--delete", src, dest]
        if exclude is not None:
            exclude_str = " ".join([f"--exclude='{e}'" for e in exclude])
            cmd_list.insert(2, exclude_str)
        if self.keyfile is not None:
            keyfile_arg = f"-i {self.keyfile}"
            cmd_list.insert(1, keyfile_arg)
        cmd_str = " ".join(cmd_list)
        logger.debug(f"Running rsync:\n{cmd_str}")
        return super().run_command(cmd_str, logger, cwd=cwd, check=True)

    def test_connection(self, logger: Logger = None, timeout: int = 5) -> bool:
        """
        Tests the connection to the remote server and the existence of the remote_base_dir.

        Returns
        -------
        bool
            True if the connection is successful and the directory exists, False otherwise.
        """
        try:
            # Pass the timeout to the remote command execution
            self.run_remote_command(
                "echo 'Trying to connect'",
                logger,
                cwd=self.local_base_dir,
                keyfile=self.keyfile,
                check=True,
                timeout=timeout,
            )
        except (RuntimeError, sp.TimeoutExpired):
            logger.error(f"Failed to connect to remote server: {self.remote_server} (timeout: {timeout}s)")
            return False
        try:
            self.run_remote_command(
                f"[ -d '{self.remote_base_dir}' ]",
                logger,
                cwd=self.local_base_dir,
                keyfile=self.keyfile,
                check=True,
                timeout=timeout,
            )
            logger.info(
                f"Successfully connected to {self.remote_server}. remote_base_dir '{self.remote_base_dir}' exists."
            )
        except (RuntimeError, sp.TimeoutExpired):
            logger.error(
                f"The remote_base_dir '{self.remote_base_dir}' does not exist on {self.remote_server} or timed out."
            )
            return False
        return True

    @overload
    def download(
        self,
        local_filepath: filepath_t,
        logger: Logger,
        *,
        exclude: Optional[Sequence[str]] = None,
        is_dir: bool = False,
        check: bool = True,
    ) -> Union[dirpath_t, filepath_t]: ...

    @overload
    def download(
        self,
        local_filepath: dirpath_t,
        logger: Logger,
        *,
        exclude: Optional[Sequence[str]] = None,
        is_dir: bool = False,
        check: bool = True,
    ) -> Union[dirpath_t, filepath_t]: ...

    def download(
        self,
        local_filepath: Union[dirpath_t, filepath_t],
        logger: Logger,
        *,
        exclude: Optional[Sequence[str]] = None,
        is_dir: bool = False,
        check: bool = True,
    ) -> Union[dirpath_t, filepath_t]:
        remote_filepath = Path(self.remote_base_dir) / Path(local_filepath).relative_to(self.local_base_dir)
        # Python honors dict ordering, so we can do this
        cmd_map = {
            "rsync": "rsync",
            "avzu": "-avzu",
            "exclude": "",
            "keyfile": "",
            "remote": f"{self.remote_server}:{remote_filepath}",
            "local": f"{local_filepath}",
        }
        isdir = Path(local_filepath).is_dir() or is_dir
        # cwd = local_filepath if isdir else local_filepath.parent
        cmd_map["remote"] += "/" if isdir else ""
        cmd_map["exclude"] = " ".join([f"--exclude='{e}'" for e in exclude]) if exclude is not None else ""
        cmd_map["keyfile"] = f'-e "ssh -i {self.keyfile}"' if self.keyfile is not None else ""

        cmd_str = " ".join([val for val in cmd_map.values() if val != ""])
        logger.debug(f"Downloading:\n{cmd_str}")
        super().run_command(cmd_str, logger, check=check)
        return local_filepath

    def get_remote_path(self, local_filepath: Union[dirpath_t, filepath_t]) -> Path:
        return Path(self.remote_base_dir) / Path(local_filepath).relative_to(self.local_base_dir)

    @overload
    def upload(
        self,
        local_filepath: filepath_t,
        logger: Logger,
        *,
        exclude: Optional[Sequence[str]] = None,
        mkdir: bool = False,
    ) -> Union[filepath_t, dirpath_t]: ...

    @overload
    def upload(
        self, local_filepath: dirpath_t, logger: Logger, *, exclude: Optional[Sequence[str]] = None, mkdir: bool = False
    ) -> Union[filepath_t, dirpath_t]: ...

    def upload(
        self,
        local_filepath: Union[dirpath_t, filepath_t],
        logger: Logger,
        *,
        exclude: Optional[Sequence[str]] = None,
        mkdir: bool = False,
    ) -> Union[filepath_t, dirpath_t]:
        remote_filepath = self.get_remote_path(local_filepath)

        if mkdir:
            mkdir_cmd = f"mkdir -p {remote_filepath.parent}"
            logger.info(f"Creating remote directory: {self.remote_server}:{remote_filepath.parent}")
            self.run_remote_command(mkdir_cmd, logger, cwd=self.local_base_dir, keyfile=self.keyfile, check=True)

        # Python honors dict ordering, so we can do this
        cmd_map = {
            "rsync": "rsync",
            "avzu": "-avzu",
            "exclude": "",
            "keyfile": "",
            "local": f"{local_filepath}",
            "remote": f"{self.remote_server}:{remote_filepath}",
        }
        isdir = Path(local_filepath).is_dir()
        # cwd = local_filepath if isdir else local_filepath.parent
        cmd_map["local"] += "/" if isdir else ""
        cmd_map["exclude"] = " ".join([f"--exclude='{e}'" for e in exclude]) if exclude is not None else ""
        cmd_map["keyfile"] = f'-e "ssh -i {self.keyfile}"' if self.keyfile is not None else ""

        cmd_str = " ".join([val for val in cmd_map.values() if val != ""])
        logger.debug(f"Uploading:\n{cmd_str}")
        super().run_command(cmd_str, logger, check=True)

        return remote_filepath

    def exists(self, local_filepath: Union[dirpath_t, filepath_t], logger: Logger) -> bool:
        """
        Checks if a file or directory exists on the remote server.

        This method uses the `test -e` command over SSH, which is a reliable
        way to check for existence on Unix-like systems.

        Args:
            local_filepath: The absolute path to the file or directory on the local FS.
            logger: A logger instance for logging the command and any potential errors.

        Returns:
            True if the path exists on the remote server, False otherwise.
        """
        # Quote the remote path to handle spaces and special characters safely
        remote_filepath = self.get_remote_path(local_filepath)
        command = f"[ -e {shlex.quote(str(remote_filepath))} ]"

        try:
            # set check=False so we don't get an error if the file/dir isn't there
            result = self.run_remote_command(
                command,
                logger,
                cwd=self.local_base_dir,  # A CWD is required, the local base is a safe default
                keyfile=self.keyfile,
                check=False,
            )
            # A return code of 0 means the 'test -e' command succeeded (the path exists).
            return result.returncode == 0
        except Exception as e:
            logger.error(f"An unexpected error occurred while checking existence of '{remote_filepath}': {e}")
            return False
