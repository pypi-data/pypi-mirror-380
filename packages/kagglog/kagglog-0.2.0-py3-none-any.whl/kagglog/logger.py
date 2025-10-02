import sys
import traceback
from datetime import datetime
from pathlib import Path


def log_exception(exc_type, exc_value, exc_traceback):
    """Logs unhandled exceptions to a file inside Kaggle working directory."""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    # Make it more flexible - detect if running in Kaggle
    error_path = _get_error_log_path()

    try:
        # Ensure directory exists
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

    # Also print to stderr
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


def _get_error_log_path():
    """Determine the appropriate error log path."""
    # Check if running in Kaggle
    kaggle_path = Path("/kaggle/working")
    if kaggle_path.exists():
        return kaggle_path / "error_log.txt"

    # Fallback to current directory
    return Path.cwd() / "error_log.txt"


def enable():
    """Enable the custom exception handler."""
    sys.excepthook = log_exception


def disable():
    """Restore the default exception handler."""
    sys.excepthook = sys.__excepthook__
