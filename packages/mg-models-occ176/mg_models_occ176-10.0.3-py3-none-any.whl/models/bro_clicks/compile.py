from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("clicks",  ["clicks.py"], extra_compile_args=["-g0"]),
    Extension("conversions", ["conversions.py"], extra_compile_args=["-g0"]),
    #Extension("load_balancer", ["load_balancer.py"], extra_compile_args=["-g0"]),
    Extension("scrub_settings", ["scrub_settings.py"], extra_compile_args=["-g0"]),
    Extension("binrouter", ["binrouter.py"], extra_compile_args=["-g0"]),
    Extension("initial_routes", ["initial_routes.py"], extra_compile_args=["-g0"]),
    Extension("splitter", ["splitter.py"], extra_compile_args=["-g0"]),
    Extension("error_log", ["error_log.py"], extra_compile_args=["-g0"]),
    Extension("aff_stats", ["aff_stats.py"], extra_compile_args=["-g0"]),
    Extension("alerts", ["alerts.py"], extra_compile_args=["-g0"]),

]
setup(
    name='bro_clicks',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
