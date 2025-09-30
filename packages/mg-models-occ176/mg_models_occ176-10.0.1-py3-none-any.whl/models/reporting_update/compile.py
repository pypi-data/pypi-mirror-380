from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("affid_report_update", ["affid_report_update.py"],extra_compile_args=["-g0"]),
    Extension("assigned_cpa_table_update", ["assigned_cpa_table_update.py"],extra_compile_args=["-g0"]),
    Extension("continuity_update", ["continuity_update.py"],extra_compile_args=["-g0"]),
    Extension("delete_duplicate", ["delete_duplicate.py"],extra_compile_args=["-g0"]),
    Extension("filter_box_updates", ["filter_box_updates.py"],extra_compile_args=["-g0"]),
    Extension("revenue_orders_update", ["revenue_orders_update.py"],extra_compile_args=["-g0"]),
    Extension("revenue_update", ["revenue_update.py"], extra_compile_args=["-g0"]),
    Extension("refund_parser", ["refund_parser.py"], extra_compile_args=["-g0"]),

]
setup(
    name='reporting_update',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
