"""Constants used throughout ``cmd2``."""

# Unless documented in https://cmd2.readthedocs.io/en/latest/api/index.html
# nothing here should be considered part of the public API of this module

INFINITY = float('inf')

# One character ellipsis
HORIZONTAL_ELLIPSIS = '…'

# For cases prior to Python 3.11 when shutil.get_terminal_size().columns can return 0.
DEFAULT_TERMINAL_WIDTH = 80
