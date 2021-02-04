import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/m-labs/lm32.git"

# Module version
version_str = "0.0.post142"
version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post142")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post57"
data_version_tuple = (0, 0, 57)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post57")
except ImportError:
    pass
data_git_hash = "84b3e3ca0ad9535acaef201c1482342871358b08"
data_git_describe = "v0.0-57-g84b3e3c"
data_git_msg = """\
commit 84b3e3ca0ad9535acaef201c1482342871358b08
Author: Michael Walle <michael@walle.cc>
Date:   Fri Oct 10 18:52:34 2014 +0200

    convert the latex documention to rst
    
    This will ease editing the documentation. For now only a HTML output is
    generated.
    
    Signed-off-by: Michael Walle <michael@walle.cc>

"""

# Tool version info
tool_version_str = "0.0.post85"
tool_version_tuple = (0, 0, 85)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post85")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_lm32."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_lm32".format(f))
    return fn
