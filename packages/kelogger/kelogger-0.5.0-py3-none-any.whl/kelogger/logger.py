# kaggle_error_logger/logger.py
import sys
import traceback
from datetime import datetime


def log_exception(exc_type, exc_value, exc_traceback):
    """Logs unhandled exceptions to a file inside Kaggle working directory."""
    if issubclass(exc_type, KeyboardInterrupt):
        # Let KeyboardInterrupts pass through without logging
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    error_path = "/kaggle/working/error_log.txt"

    try:
        with open(error_path, "a") as f:  # "a" for append mode
            f.write(f"\n{'='*60}\n")
            f.write(
                f"Exception at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("Unhandled Exception:\n")
            traceback.print_exception(
                exc_type, exc_value, exc_traceback, file=f)
    except Exception as e:
        # If logging fails, at least print to stderr
        print(f"Failed to write to error log: {e}", file=sys.stderr)

    # Also print to stderr (so it shows in Kaggle UI logs)
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


def enable():
    """Enable the custom exception handler."""
    sys.excepthook = log_exception


def disable():
    """Restore the default exception handler."""
    sys.excepthook = sys.__excepthook__
    """Enable the error logger by setting a custom excepthook."""
    sys.excepthook = log_exception
