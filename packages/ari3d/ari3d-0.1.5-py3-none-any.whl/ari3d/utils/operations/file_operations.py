"""Module for file operations used in the ARI3D project."""
import errno
import os
import platform
import shutil
import stat
import sys
import time
from pathlib import Path
from typing import Any, Optional, Union

import yaml

enc = sys.getfilesystemencoding()
win_shell = None


def get_dict_from_yml(yml_file):
    """Read a dictionary from a file in yml format."""
    with open(yml_file) as yml_f:
        d = yaml.safe_load(yml_f)

    if not isinstance(d, dict):
        raise TypeError("Yaml file %s invalid!" % str(yml_file))

    return d


def write_dict_to_yml(yml_file, d):
    """Write a dictionary to a file in yml format."""
    yml_file = Path(yml_file)
    create_path_recursively(yml_file.parent)

    with open(yml_file, "w+") as yml_f:
        yml_f.write(yaml.dump(d, Dumper=yaml.Dumper))

    return True


def create_path_recursively(path):
    """Create a path. Creates missing parent folders."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)

    return True


def copy_folder(
    folder_to_copy, destination, copy_root_folder=True, force_copy=False, logger=None
) -> Path:
    """Copy a folder to a destination.

    Args:
        folder_to_copy:
            The folder to copy
        destination:
            The destination folder to copy to
        copy_root_folder:
            boolean value. if true copies the root folder in the target destination.
            Else all files in the folder to copy.
        force_copy:
            boolean value. If true, removes the destination folder before copying.

    """
    folder_to_copy = Path(folder_to_copy)
    destination = Path(destination)

    if os.path.exists(destination) and os.path.samefile(folder_to_copy, destination):
        return destination

    if copy_root_folder:
        destination = destination.joinpath(folder_to_copy.name)

    if force_copy:
        force_remove(destination, logger=logger)

    create_path_recursively(destination)

    for root, dirs, files in os.walk(folder_to_copy):
        root = Path(root)

        for d in dirs:
            copy_folder(
                root.joinpath(d), destination.joinpath(d), copy_root_folder=False
            )
        for fi in files:
            copy(root.joinpath(fi), destination)
        break

    return destination


def copy(file, path_to) -> Path:
    """Copy a file A to either folder B or file B. Makes sure folder structure for target exists."""
    file = Path(file)
    path_to = Path(path_to)

    if os.path.exists(path_to) and os.path.samefile(file, path_to):
        return path_to

    create_path_recursively(path_to.parent)

    return Path(shutil.copy(file, path_to))


def force_remove(path, logger, warning=True, retries=3, delay=0.5):
    """Force remove a file or folder. If the path is read-only, it will be made writable first."""
    path = Path(path)

    if not path.exists():
        return

    for attempt in range(1, retries + 1):
        try:
            if path.is_file():
                path.unlink()
            else:
                shutil.rmtree(
                    str(path), ignore_errors=False, onerror=handle_remove_readonly
                )
            return  # success
        except PermissionError:
            logger.warning("PermissionError on deleting %s (attempt %d)", path, attempt)
            handle_remove_readonly(
                os.unlink if path.is_file() else None, path, sys.exc_info()
            )
        except Exception as e:
            if attempt == retries:
                logger.exception(
                    "Failed to force remove %s after %d attempts", path, retries
                )
                if not warning:
                    raise
            else:
                logger.warning(
                    "Retrying delete of %s (attempt %d): %s", path, attempt, e
                )

        time.sleep(delay * attempt)


def handle_remove_readonly(func, path, exc):
    """Change readonly flag of a given path."""
    excvalue = exc[1]
    if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        raise


def copy_tiffs(
    images_files,
    img_src_path: Path,
    gray_path: Path,
    logger,
    retries=5,
    base_delay=0.2,
    symlinks=True,
):
    """Copy tiff files from project_path to gray_path, then delete originals."""
    files = list(images_files)  # materialize in case it's a generator
    gray_path.mkdir(parents=True, exist_ok=True)

    if symlinks:
        task_str = "symlinking"
    else:
        task_str = "copying"

    logger.info("%s %d tiff files to grey folder...", task_str, len(files))
    for i, image_file in enumerate(files, 1):
        src = img_src_path.joinpath(image_file)
        dst = gray_path.joinpath(image_file)

        logger.debug("Processing file %d/%d: %s -> %s", i, len(files), src, dst)

        for attempt in range(1, retries + 1):
            try:
                # Ensure destination folder exists
                create_path_recursively(dst.parent)

                if symlinks:
                    # we want to point from dst to its src, thereby creating dst, src must exist
                    create_symlink(dst, src, create=True)
                else:
                    # Copy first
                    shutil.copy2(src, dst)

                break  # success
            except PermissionError:
                # Likely locked by another process; wait & retry
                if attempt == retries:
                    logger.exception("Locked file, giving up: %s", src)
                    raise
                time.sleep(base_delay * attempt)
            except Exception:
                logger.exception("Failed to %s: %s -> %s", task_str, src, dst)
                raise


def create_symlink(
    point_from: Path, point_to: Path, create: bool = True
) -> Optional[Path]:
    """Construct a link from point_from to point_to.

    Args:
        point_from:
            Path where to point from.
        point_to:
            File Path where to point to. Must exist!
        create:
            Flag indicating whether to create the link.

    Returns:
        Path to the resolved link.

    """
    operation_system = platform.system().lower()

    if "windows" in operation_system:
        point_from_ = point_from.parent.joinpath(
            point_from.stem + ".lnk"
        )  # .lnk extension
        if point_from_.exists():
            return _get_shortcut_target(point_from_)
        if create:
            if not point_to.exists():
                raise FileNotFoundError(
                    f"Target path {point_to} does not exist. Cannot create shortcut {point_from_} to it."
                )
            create_path_recursively(point_from_.parent)

            _create_shortcut(point_from_, target=point_to)
            resolve = point_to.absolute()
            return resolve
    else:
        if os.path.islink(point_from):
            r = Path(point_from).resolve()

            if not r.exists():
                create_path_recursively(r)

            return r
        if create:
            create_path_recursively(Path(point_from).parent)

            # point_from -> point_to
            os.symlink(str(point_to), point_from, target_is_directory=False)
            return point_to.resolve()

    return Path("")


def _get_shortcut_target(shortcut_path: Union[str, Path]) -> Path:
    """Get the target of a shortcut."""
    shortcut_path = Path(shortcut_path)
    if not shortcut_path.parent.exists():
        raise LookupError("Shortcut %s doesn't exist." % shortcut_path)

    sh = _get_global_win_shell()
    wscript = sh.CreateShortCut(str(shortcut_path.absolute()))
    return Path(wscript.TargetPath)


def _get_global_win_shell() -> Any:
    """Get the global windows shell."""
    global win_shell
    import win32com.client

    if win_shell is None:
        win_shell = win32com.client.Dispatch("Wscript.Shell")
    return win_shell


def _create_shortcut(shortcut_path: Union[str, Path], target: Union[str, Path]) -> None:
    """Create a shortcut file pointing to a given target."""
    shortcut_path = Path(shortcut_path)
    if not shortcut_path.parent.exists():
        shortcut_path.parent.mkdir(parents=True, exist_ok=True)
    sh = _get_global_win_shell()
    wscript = sh.CreateShortCut(str(shortcut_path.absolute()))
    wscript.TargetPath = str(Path(target).absolute())
    wscript.save()
