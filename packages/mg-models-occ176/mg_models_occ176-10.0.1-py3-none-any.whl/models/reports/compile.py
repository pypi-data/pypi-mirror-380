from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("widgets", ["widgets.py"], extra_compile_args=["-g0"]),
   # Extension("table_reports", ["table_reports.py"], extra_compile_args=["-g0"]),
    Extension("traffic", ["traffic.py"], extra_compile_args=["-g0"]),
    Extension("dependencies", ["dependencies.py"], extra_compile_args=["-g0"]),
    Extension("cap", ["cap.py"], extra_compile_args=["-g0"]),
    Extension("traffic_reporting", ["traffic_reporting.py"], extra_compile_args=["-g0"]),
    Extension("reporting_alerts", ["reporting_alerts.py"], extra_compile_args=["-g0"]),

]
setup(
    name='reports',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)