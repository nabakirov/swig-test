
"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


example_module = Extension('_GeoCore',
                           sources=['GeoCore_wrap.cxx', 'GeoCore.cpp'],
                           )

setup (name = 'geocore',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )