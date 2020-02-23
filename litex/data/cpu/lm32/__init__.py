import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/m-labs/lm32.git"
git_hash = "84b3e3ca0ad9535acaef201c1482342871358b08"
git_describe = "v0.0-57-g84b3e3c"
version = "0.0.57"
version_tuple = (0, 0, 57)
try:
    from packaging.version import Version as V
    pversion = V("0.0.57")
except ImportError:
    pass