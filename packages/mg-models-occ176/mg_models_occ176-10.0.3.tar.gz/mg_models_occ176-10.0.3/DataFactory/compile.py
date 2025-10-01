from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [

    Extension("sqlinterface", ["sqlinterface.py"],extra_compile_args = ["-g0"]),

#   ... all your modules that need be compiled ...
]
setup(
    name = 'DataFactory',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
