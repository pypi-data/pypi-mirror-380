import inspect
import json
import os
import shutil
import subprocess
import warnings
from pathlib import Path
from typing import Any, get_args, get_origin, overload


def _get_utils_path() -> Path:
    """Returns the path to envsh-utils.sh script for shell scripts."""
    return Path(__file__).parent / "envsh-utils.sh"


def _apply_shell_environment(script_path: Path) -> None:
    """Applies environment variables from shell script to current process."""
    try:
        if os.name == "nt":
            executable = shutil.which("bash")
            if not executable:
                raise RuntimeError("bash.exe not founded. Install Git Bash or MSYS2 and add to PATH.")
            unix_path = str(script_path.resolve()).replace('\\', '/').replace('C:', '/c')
            command = [executable, "-c", f"source '{_get_utils_path()}' && source '{unix_path}' 2>/dev/null && printenv -0"]
        elif os.name == "posix":
            executable = '/bin/bash'
            command = [executable, "-c", f"source '{_get_utils_path()}' && source '{script_path.resolve()}' > /dev/null && printenv -0"]

        result = subprocess.run(
            command,
            shell=False,
            capture_output=True,
            check=True,
            text=False
        )
        env_vars = result.stdout.strip(b'\0').split(b'\0')
        for var_line_bytes in env_vars:
            if not var_line_bytes:
                continue
            var_line = var_line_bytes.decode('utf-8')
            if '=' in var_line:
                key, value = var_line.split('=', 1)
                os.environ[key] = value
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise RuntimeError(f"Failed to load using {executable} environment from {script_path}: {e}") from e


def load(search_paths: list[str] | None = None, verbose: bool = False) -> bool:
    """Loads environment variables from .sh files in specified directories."""
    frame = inspect.currentframe()
    caller_frame = frame.f_back if frame else None
    caller_file = caller_frame.f_globals.get('__file__') if caller_frame else None
    caller_dir = Path(caller_file).parent.resolve() if caller_file else Path('.').resolve()

    if search_paths is None:
        search_paths = [str(caller_dir)]
    else:
        search_paths = [
            str((caller_dir / p).resolve()) if not Path(p).is_absolute() else str(Path(p).resolve())
            for p in search_paths
        ]

    if verbose:
        print(f"\nSearch paths: {search_paths}")

    found_files = set()
    for path_str in search_paths:
        path_obj = Path(path_str)
        if not path_obj.exists():
            continue
        for sh_file in path_obj.glob('*.sh'):
            found_files.add(sh_file.resolve())

    if not found_files:
        if verbose:
            print("No .sh files found in search paths")
        return False

    sorted_files = sorted(list(found_files))

    if verbose:
        print(f"Found {len(sorted_files)} .sh file(s):")
        for file_path in sorted_files:
            print(f"  -> {file_path}")

    for file_path in sorted_files:
        try:
            _apply_shell_environment(file_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load environment from {file_path}: {e}") from e

    return True


# Type overloads for proper typing

@overload
def read_env(name: str) -> str: ...

@overload
def read_env(name: str, default: str | None = None) -> str: ...

@overload
def read_env(name: str, return_type: type[int], default: int | None = None) -> int: ...

@overload
def read_env(name: str, return_type: type[float], default: float | None = None) -> float: ...

@overload
def read_env(name: str, return_type: type[str], default: str | None = None) -> str: ...

@overload
def read_env(name: str, return_type: type[list[int]], default: list[int] | None = None) -> list[int]: ...

@overload
def read_env(name: str, return_type: type[list[str]], default: list[str] | None = None) -> list[str]: ...

@overload
def read_env(name: str, return_type: type[dict[Any, Any]], default: dict[Any, Any] | None = None) -> dict[Any, Any]: ...


def read_env( # type: ignore[misc]
    name: str,
    return_type: type = str,
    default: Any = None
) -> int | str | list[int] | list[str] | float | dict[Any, Any]:
    """Reads environment variable with specified return type."""
    value = os.getenv(name)
    if value is None:
        if default is not None:
            warnings.warn(
                f"Environment variable '{name}' is not set. Returning default value: {default!r}",
                stacklevel=2
            )
            if return_type is int:
                return int(default) if default is not None else 0
            elif return_type is float:
                return float(default) if default is not None else 0.0
            elif return_type is str:
                return str(default) if default is not None else ""
            origin = get_origin(return_type)
            args = get_args(return_type)
            if origin is list and args:
                subtype = args[0]
                if subtype is int:
                    return list(default) if default is not None else []
                elif subtype is str:
                    return list(default) if default is not None else []
            elif return_type is dict:
                return dict(default) if default is not None else {}
            raise TypeError(f"Unsupported return type: {return_type}")
        raise OSError(f"The environment variable '{name}' is not set.")

    origin = get_origin(return_type)
    args = get_args(return_type)

    if return_type is int:
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"The environment variable '{name}' contains non-integer value: '{value}'") from None
    elif return_type is float:
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"The environment variable '{name}' contains non-float value: '{value}'") from None
    elif return_type is str:
        return str(value)
    elif origin is list and args:
        subtype = args[0]
        if subtype is int:
            if not value.strip():
                return []
            try:
                return [int(item.strip()) for item in value.split(',') if item.strip()]
            except ValueError:
                raise ValueError(f"The environment variable '{name}' contains non-integer values: '{value}'") from None
        elif subtype is str:
            if not value.strip():
                return []
            return [item.strip() for item in value.split(',') if item.strip()]
        else:
            raise TypeError(f"Unsupported list subtype: {subtype}")
    elif return_type is dict:
        try:
            return dict(json.loads(value))
        except json.JSONDecodeError:
            raise ValueError(f"The environment variable '{name}' contains invalid JSON: '{value}'") from None
    else:
        raise TypeError(f"Unsupported return type: {return_type}")

