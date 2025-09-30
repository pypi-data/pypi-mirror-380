# __init__.py
"""
mypackage: Python bindings with C++ extension and resources.
"""

import os, sys
# C++ extension module (built via pybind11_add_module(libcalab ...))
try:
    from . import libmainlib as m
except ImportError as e:
    raise ImportError("Failed to import C++ extension 'libmainlib'. "
                      "Did you build and install the wheel correctly?") from e
# 표준 에러 무시
tempErr=sys.stderr
sys.stderr = open(os.devnull, 'w')
try:
    import settings
except ModuleNotFoundError:
    try:
        import work.settings as settings
        settings.relativeMode=True

    except ModuleNotFoundError:  # work path doesn't exist so we have to use internal resources
        from . import default_settings as settings
        settings.relativeMode=True
        package_dir = os.path.dirname(os.path.abspath(__file__))
        print('taesooLibPath:', package_dir)
        m.setTaesooLibPath(package_dir+"/")


settings.mlib=m
try:
    from . import luamodule as lua
    settings.lua=lua
    from . import rendermodule as RE
    settings.RE=RE
    from . import controlmodule as control
    settings.control=control
except ImportError as e:
    raise ImportError("Failed to import python extensions 'luamodule, rendermodule, controlmodule'. "
                      "Did you build and install the wheel correctly?") from e


sys.stderr=tempErr

