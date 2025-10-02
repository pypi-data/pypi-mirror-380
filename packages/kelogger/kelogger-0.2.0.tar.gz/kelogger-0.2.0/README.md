# Kaggle Error Logger

`kaggle_error_logger` is a lightweight Python package that automatically logs **unhandled exceptions** in Kaggle notebooks or scripts. Any uncaught error is saved to a file (`/kaggle/working/error_log.txt`) so it can be accessed by monitoring tools or for debugging purposes. This is especially useful when running long Kaggle kernels where errors might otherwise be missed.

---

## Features

- Automatically captures **unhandled exceptions** in Kaggle kernels.
- Saves **full Python traceback** to `/kaggle/working/error_log.txt`.
- Works without modifying user code extensively—just a simple import and enable.
- Compatible with **Kaggle notebooks and scripts**.
- Integrates with external monitoring tools (like automated email notifications or fix agents).

---

## Installation

Install directly from PyPI:

```bash
pip install kaggle_error_logger
```
