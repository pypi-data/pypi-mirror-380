"""Logging module with robust error capture (tee to console + file)."""

import atexit
import io
import logging
import os
import sys
import threading
import time
from contextlib import contextmanager
from pathlib import Path

from ari3d import __version__ as ari3d_version

try:
    import asyncio
except Exception:
    asyncio = None

LOGGER_NAME = "ARI3D"
CALL_TIME = None


def _safe_orig_stream(which: str):
    # Try sys.stdout / sys.stderr; fall back to sys.__stdout__/__stderr__; else /dev/null
    s = getattr(sys, which, None)
    if s is None:
        s = getattr(sys, f"__{which}__", None)
    if s is None:
        # no console (e.g., pythonw.exe) – use a dummy file that accepts writes
        return open(os.devnull, "w", encoding="utf-8", buffering=1)
    return s


# Keep originals so we can tee without losing console output
_ORIG_STDOUT = _safe_orig_stream("stdout")
_ORIG_STDERR = _safe_orig_stream("stderr")

_orig_exit = sys.exit


def _logging_exit(code=0):
    get_logger().error("sys.exit called: code=%r", code)
    _orig_exit(code)


sys.exit = _logging_exit


def get_log_file_prefix() -> str:
    """Get a log file prefix based on the first call time."""
    global CALL_TIME
    if not CALL_TIME:
        CALL_TIME = time.strftime("%Y%m%d_%H-%M-%S")
    return f"run_{CALL_TIME}"


def get_logger() -> logging.Logger:
    """Get the application logger (singleton)."""
    return logging.getLogger(LOGGER_NAME)


class _MaxLevelFilter(logging.Filter):
    """Allow records up to a maximum level (inclusive)."""

    def __init__(self, max_level: int):
        super().__init__()
        self.max_level = max_level

    def filter(self, record: logging.LogRecord) -> bool:  # noqa: A003
        """Allow records up to a maximum level (inclusive)."""
        return record.levelno <= self.max_level


def get_default_formatter():
    """Get a default formatter."""
    return logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )


def _attach_file_to_root(logfile_name, formatter):
    """Attach ONE FileHandler at DEBUG to the ROOT logger (catch-all)."""
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    # avoid duplicates for same file
    for h in root.handlers:
        if isinstance(h, logging.FileHandler) and getattr(h, "baseFilename", "") == str(
            logfile_name
        ):
            return h
    fh = logging.FileHandler(str(logfile_name), mode="a", encoding="utf-8", delay=False)
    fh.setLevel(logging.DEBUG)  # <-- never reduced; captures everything
    fh.setFormatter(formatter)
    root.addHandler(fh)
    return fh


class _TeeToLogger(io.TextIOBase):
    """Tee to the original text stream and to a logger (which propagates to root->file).

    Behaves like a real text stream: proxies fileno/encoding/errors/newlines/buffer/etc.
    """

    def __init__(self, orig_stream, capture_logger: logging.Logger, level: int):
        self._orig = orig_stream
        self._cap = capture_logger
        self._level = level
        self._buf = ""

    # ---- write/flush ----
    def write(self, s):
        if not isinstance(s, str):
            s = s.decode(errors="replace")
        # 1) console
        try:
            self._orig.write(s)
        except Exception:
            pass
        # 2) logger (line-buffered)
        self._buf += s
        while "\n" in self._buf:
            line, self._buf = self._buf.split("\n", 1)
            self._cap.log(self._level, line)
        return len(s)

    def flush(self):
        try:
            self._orig.flush()
        except Exception:
            pass
        if self._buf:
            self._cap.log(self._level, self._buf)
            self._buf = ""

    # ---- stream-like behavior ----
    def fileno(self):
        if hasattr(self._orig, "fileno"):
            return self._orig.fileno()
        raise io.UnsupportedOperation("fileno")

    def isatty(self):
        try:
            return bool(self._orig.isatty())
        except Exception:
            return False

    def readable(self):
        return False

    def writable(self):
        return True

    def seekable(self):
        return False

    def close(self):
        # don't close the original; just flush our buffer
        self.flush()

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    # ---- read-only proxy properties ----
    @property
    def encoding(self):
        return getattr(self._orig, "encoding", "utf-8")

    @property
    def errors(self):
        return getattr(self._orig, "errors", "backslashreplace")

    @property
    def newlines(self):
        return getattr(self._orig, "newlines", None)

    @property
    def buffer(self):
        return getattr(self._orig, "buffer", None)

    @property
    def closed(self):
        return getattr(self._orig, "closed", False)

    # ---- forward everything else to the original ----
    def __getattr__(self, name):
        return getattr(self._orig, name)


def _get_capture_logger() -> logging.Logger:
    """Logger used only for tee/exception capture; NO handlers on it.

    It just propagates to ROOT (which has the file handler).
    """
    cap = logging.getLogger(f"{LOGGER_NAME}.CAPTURE")
    cap.setLevel(logging.DEBUG)
    cap.propagate = True
    # Ensure no direct handlers that could write back into our tee
    for h in list(cap.handlers):
        cap.removeHandler(h)
    return cap


def _install_global_exception_hooks():
    """Route uncaught exceptions to logging AND still show default console traceback."""
    cap = _get_capture_logger()

    def _print_default_tb_to_real_console(exc_type, exc_value, exc_traceback):
        # Print using the real console, not our tee, to avoid loops
        _tmp = sys.stderr
        try:
            sys.stderr = _ORIG_STDERR
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
        finally:
            sys.stderr = _tmp

    def handle_exception(exc_type, exc_value, exc_traceback):
        """Handle uncaught exceptions."""
        if issubclass(exc_type, KeyboardInterrupt):
            _print_default_tb_to_real_console(exc_type, exc_value, exc_traceback)
            return
        # Structured record into file
        cap.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
        # Human-readable traceback to real console
        _print_default_tb_to_real_console(exc_type, exc_value, exc_traceback)

    sys.excepthook = handle_exception

    # Threads (3.8+)
    if hasattr(threading, "excepthook"):

        def thread_excepthook(args: threading.ExceptHookArgs):
            cap.error(
                "Uncaught exception in thread %s",
                getattr(args, "thread", None).name
                if getattr(args, "thread", None)
                else "<unknown>",
                exc_info=(args.exc_type, args.exc_value, args.exc_traceback),
            )
            _print_default_tb_to_real_console(
                args.exc_type, args.exc_value, args.exc_traceback
            )

        threading.excepthook = thread_excepthook

    # asyncio (if used)
    if asyncio is not None:
        try:
            loop = asyncio.get_event_loop()

            def async_handler(loop, context):
                msg = context.get("message", "Unhandled asyncio exception")
                exc = context.get("exception")
                if exc:
                    cap.error(msg, exc_info=(type(exc), exc, exc.__traceback__))
                else:
                    cap.error("%s: %s", msg, context)
                _ORIG_STDERR.write(msg + "\n")

            loop.set_exception_handler(async_handler)
        except Exception:
            pass


# add this helper + filter near your other helpers
def _make_file_handler(path, formatter, level=logging.DEBUG):
    fh = logging.FileHandler(str(path), mode="a", encoding="utf-8", delay=False)
    fh.setLevel(level)
    fh.setFormatter(formatter)
    return fh


class _DropPrefixFilter(logging.Filter):
    """Drop records whose logger name starts with the given prefix."""

    def __init__(self, prefix: str):
        super().__init__()
        self.prefix = prefix

    def filter(self, record: logging.LogRecord) -> bool:  # noqa: A003
        """Drop records whose logger name starts with the given prefix."""
        return not (
            record.name == self.prefix or record.name.startswith(self.prefix + ".")
        )


def configure_logger(loglevel="INFO", logfile_name=None, formatter_string=None):
    """Configure the application logger.

    - console handlers write to ORIGINAL stdout/stderr
    - root has the file handler at DEBUG (captures all libs and capture logger)
    - app logger propagates so its messages also land in the file
    """
    logger = get_logger()

    # clear existing handlers...
    for h in list(logger.handlers):
        try:
            h.close()
        except Exception:
            pass
        logger.removeHandler(h)

    # IMPORTANT: never drop records at the logger
    logger.setLevel(logging.DEBUG)  # <-- change from logger.setLevel(loglevel)

    # formatter
    formatter = (
        get_default_formatter()
        if not formatter_string
        else logging.Formatter(formatter_string)
    )

    # parse requested console level
    console_level = (
        logging._nameToLevel.get(loglevel, logging.INFO)
        if isinstance(loglevel, str)
        else int(loglevel)
    )

    # stdout handler (<= WARNING to stdout)
    stdout_handler = logging.StreamHandler(stream=_ORIG_STDOUT)
    stdout_handler.setLevel(console_level)  # <-- use console_level here
    stdout_handler.addFilter(_MaxLevelFilter(logging.WARNING))
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    # stderr handler (ERROR+)
    stderr_handler = logging.StreamHandler(stream=_ORIG_STDERR)
    stderr_handler.setLevel(logging.ERROR)
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stderr_handler)

    # File handler on ROOT at DEBUG (already correct)
    if logfile_name:
        # 1) File handler on ARI3D (your app)
        fh_app = _make_file_handler(logfile_name, formatter, level=logging.DEBUG)
        logger.addHandler(fh_app)
        # 2) File handler on ROOT (all libs, capture logger, etc)
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        fh_root = _make_file_handler(logfile_name, formatter, level=logging.DEBUG)
        fh_root.addFilter(_DropPrefixFilter(LOGGER_NAME))
        root.addHandler(fh_root)

    # ARI3D logs directly to its own file handler; don’t propagate to root
    logger.propagate = False

    logger.propagate = True
    logging.captureWarnings(True)
    return logger


def close_logger():
    """Restore real streams, close app handlers (root file handler can remain)."""
    # Restore original streams
    if sys.stdout is not _ORIG_STDOUT:
        sys.stdout = _ORIG_STDOUT
    if sys.stderr is not _ORIG_STDERR:
        sys.stderr = _ORIG_STDERR

    logger = get_logger()
    for h in list(logger.handlers):
        try:
            h.flush()
            h.close()
        except Exception:
            pass
        logger.removeHandler(h)


atexit.register(close_logger)


class Ari3dLogger:
    """Ari3d logger class (singleton)."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Create or return the singleton instance."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def _initialize(self, loglevel="INFO", formatter_string=None):
        base_log_path = Path.home() / ".ari3d"
        base_log_path.mkdir(parents=True, exist_ok=True)

        self.log_file_path = base_log_path / f"ari3d_{get_log_file_prefix()}.log"
        self.log = configure_logger(
            loglevel=loglevel,
            logfile_name=str(self.log_file_path),
            formatter_string=formatter_string,
        )

        # Capture uncaught exceptions AND keep console tracebacks
        _install_global_exception_hooks()

        # Tee stdout/stderr: console + file (through capture logger propagating to root)
        cap = _get_capture_logger()
        self.log.debug("Installing stdout/stderr tee...")
        try:
            sys.stdout = _TeeToLogger(_ORIG_STDOUT, cap, logging.DEBUG)
            sys.stderr = _TeeToLogger(_ORIG_STDERR, cap, logging.ERROR)
            self.log.debug("Stdout/stderr tee installed.")
        except Exception:
            # If tee breaks in this environment, keep running without it.
            logger = get_logger()
            logger.exception(
                "Failed to install stdout/stderr tee; continuing without tee."
            )
            # Do NOT replace sys.stdout/err; leave originals intact.

        # version info
        self.log.info("ARI3D version: %s", ari3d_version)

    def set_log_level(self, loglevel):
        """Change verbosity of the app logger console; file remains at DEBUG via root."""
        for h in self.log.handlers:
            if isinstance(h, logging.StreamHandler):
                # stderr handler stays at ERROR; stdout follows requested level
                if getattr(h, "stream", None) is _ORIG_STDERR:
                    h.setLevel(logging.ERROR)
                else:
                    h.setLevel(loglevel)

    def set_log_level_info(self):
        """Set the loglevel to INFO."""
        self.log.info("Set loglevel to INFO...")
        self.set_log_level(logging.INFO)

    def set_log_level_debug(self):
        """Set the loglevel to DEBUG."""
        self.log.info("Set loglevel to DEBUG...")
        self.set_log_level(logging.DEBUG)

    def set_log_level_warning(self):
        """Set the loglevel to WARNING."""
        self.log.info("Set loglevel to WARNING...")
        self.set_log_level(logging.WARNING)

    def set_log_level_none(self):
        """Disable logging."""
        self.log.info("Disable logging to console...")
        self.log.disabled = True


@contextmanager
def log_unhandled(logger: logging.Logger, where: str = "app"):
    """Context manager to log unhandled exceptions in a block of code."""
    try:
        yield
    except SystemExit as e:
        logger.error("SystemExit in %s: code=%r", where, getattr(e, "code", None))
        raise
    except KeyboardInterrupt:
        logger.error("KeyboardInterrupt in %s", where)
        raise
    except GeneratorExit:
        logger.error("GeneratorExit in %s", where)
        raise
    except BaseException:
        logger.error("Unhandled exception in %s", where, exc_info=True)
        raise
