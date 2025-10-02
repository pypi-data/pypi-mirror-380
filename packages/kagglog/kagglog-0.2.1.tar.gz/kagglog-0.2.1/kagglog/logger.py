import sys
import traceback
from datetime import datetime
from pathlib import Path


def log_exception(exc_type, exc_value, exc_traceback):
    """Logs unhandled exceptions to a file inside Kaggle working directory."""
    if issubclass(exc_type, KeyboardInterrupt):
        return None  # Let it pass through

    error_path = _get_error_log_path()

    try:
        Path(error_path).parent.mkdir(parents=True, exist_ok=True)

        with open(error_path, "a") as f:
            f.write(f"\n{'='*60}\n")
            f.write(
                f"Exception at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("Unhandled Exception:\n")
            traceback.print_exception(
                exc_type, exc_value, exc_traceback, file=f)
    except Exception as e:
        print(f"Failed to write to error log: {e}", file=sys.stderr)


def _get_error_log_path():
    """Determine the appropriate error log path."""
    kaggle_path = Path("/kaggle/working")
    if kaggle_path.exists():
        return kaggle_path / "error_log.txt"
    return Path.cwd() / "error_log.txt"


def enable():
    """Enable the custom exception handler."""
    # Try to hook into IPython/Jupyter first
    try:
        from IPython import get_ipython
        ipython = get_ipython()

        if ipython is not None:
            # Store original handler
            original_handler = ipython.excepthook

            def custom_ipython_handler(shell, exc_type, exc_value, exc_traceback, tb_offset=None):
                # Log the exception
                log_exception(exc_type, exc_value, exc_traceback)
                # Call original handler to display in notebook
                if original_handler:
                    original_handler(shell, exc_type, exc_value,
                                     exc_traceback, tb_offset)

            ipython.set_custom_exc((Exception,), custom_ipython_handler)
            return
    except (ImportError, AttributeError):
        pass

    # Fallback to regular sys.excepthook for non-notebook environments
    sys.excepthook = lambda exc_type, exc_value, exc_traceback: (
        log_exception(exc_type, exc_value, exc_traceback),
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
    )


def disable():
    """Restore the default exception handler."""
    try:
        from IPython import get_ipython
        ipython = get_ipython()

        if ipython is not None:
            ipython.set_custom_exc(tuple(), None)
            return
    except (ImportError, AttributeError):
        pass

    sys.excepthook = sys.__excepthook__
