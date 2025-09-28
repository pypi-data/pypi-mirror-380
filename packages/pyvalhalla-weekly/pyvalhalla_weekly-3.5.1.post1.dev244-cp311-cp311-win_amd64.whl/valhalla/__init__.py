"""""" # start delvewheel patch
def _delvewheel_patch_1_10_1():
    import os
    if os.path.isdir(libs_dir := os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pyvalhalla_weekly.libs'))):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_10_1()
del _delvewheel_patch_1_10_1
# end delvewheel patch

from pathlib import Path

try:
    from ._valhalla import VALHALLA_PRINT_VERSION, VALHALLA_PYTHON_PACKAGE
except ModuleNotFoundError:
    from _valhalla import VALHALLA_PRINT_VERSION, VALHALLA_PYTHON_PACKAGE
from .actor import Actor
from .config import get_config, get_help

# if run from CMake, Docker or test
try:
    from .__version__ import __version__

    # extend with version modifier (so far the git hash)
    if (idx := VALHALLA_PRINT_VERSION.find("-")) != -1:
        __version__ = __version__ + VALHALLA_PRINT_VERSION[idx:]
except ModuleNotFoundError:
    __version__ = "undefined"

PYVALHALLA_DIR = Path(__file__).parent.resolve()

__all__ = ["Actor", "get_config", "get_help", "__version__"]
