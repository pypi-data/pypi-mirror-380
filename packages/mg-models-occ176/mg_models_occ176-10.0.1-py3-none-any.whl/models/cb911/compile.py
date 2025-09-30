from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("cb_struc", ["cb_struc.py"], extra_compile_args=["-g0"]),
    Extension("chargebacks",  ["chargebacks.py"], extra_compile_args=["-g0"]),
    Extension("alerts", ["alerts.py"], extra_compile_args=["-g0"]),

]
setup(
    name='models',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)