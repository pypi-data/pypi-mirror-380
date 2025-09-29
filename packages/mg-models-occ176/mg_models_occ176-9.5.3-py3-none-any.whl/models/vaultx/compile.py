from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("ssc_cont", ["ssc_cont.py"], extra_compile_args=["-g0"]),

]
setup(
    name='models',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)