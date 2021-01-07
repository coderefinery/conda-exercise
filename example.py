import sys
from distutils.version import LooseVersion

try:
    from numpy import __version__ as numpy_version
except ModuleNotFoundError:
    sys.exit("ERROR: could not find numpy")

try:
    from pandas import __version__ as pandas_version
except ModuleNotFoundError:
    sys.exit("ERROR: could not find pandas")

if not LooseVersion("1.14") <= LooseVersion(numpy_version) < LooseVersion("1.16"):
    sys.exit(
        "ERROR: numpy version unfortunately does not match, yours is " + numpy_version
    )

if not LooseVersion("0.23") <= LooseVersion(pandas_version) < LooseVersion("0.26"):
    sys.exit(
        "ERROR: pandas version unfortunately does not match, yours is " + pandas_version
    )

print("Yay! You managed to install matching versions! Congrats!")
