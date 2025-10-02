# kaggle_error_logger/logger.py
import sys
import traceback


def log_exception(exc_type, exc_value, exc_traceback):
    """Logs unhandled exceptions to a file inside Kaggle working directory."""
    if issubclass(exc_type, KeyboardInterrupt):
        # Let KeyboardInterrupts pass through without logging
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    error_path = "/kaggle/working/error_log.txt"
    with open(error_path, "w") as f:
        f.write("Unhandled Exception:\n")
        traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)

    # Also print to stderr (so it shows in Kaggle UI logs)
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


def enable():
    """Enable the error logger by setting a custom excepthook."""
    sys.excepthook = log_exception
