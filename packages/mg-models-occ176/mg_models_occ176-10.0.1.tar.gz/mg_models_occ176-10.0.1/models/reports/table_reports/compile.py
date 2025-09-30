from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("affid_report", ["affid_report.py"], extra_compile_args=["-g0"]),
    Extension("mtd_report", ["mtd_report.py"], extra_compile_args=["-g0"]),
    Extension("inactive_report", ["inactive_report.py"], extra_compile_args=["-g0"]),
Extension("impact_reports", ["impact_reports.py"], extra_compile_args=["-g0"]),
    Extension("continuity_report", ["continuity_report.py"], extra_compile_args=["-g0"]),
    Extension("bin_report", ["bin_report.py"], extra_compile_args=["-g0"]),
    Extension("approval_report", ["approval_report.py"], extra_compile_args=["-g0"]),

]
setup(
    name='table_reports',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)