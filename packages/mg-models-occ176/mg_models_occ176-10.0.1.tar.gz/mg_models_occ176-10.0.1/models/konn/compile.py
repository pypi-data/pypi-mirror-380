from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    #Extension("__init__",  ["__init__.py"]),


    Extension("campaigns",  ["campaigns.py"], extra_compile_args = ["-g0"]),
    Extension("hybrid", ["hybrid.py"], extra_compile_args=["-g0"]),
    Extension("gateways", ["gateways.py"], extra_compile_args=["-g0"]),
    Extension("orders",  ["orders.py"], extra_compile_args = ["-g0"]),
    Extension("composite",  ["composite.py"], extra_compile_args = ["-g0"]),
    Extension("customers",  ["customers.py"], extra_compile_args = ["-g0"]),
    Extension("config", ["config.py"], extra_compile_args=["-g0"]),

    Extension("fullfillment_items", ["fullfillment_items.py"], extra_compile_args=["-g0"]),
    Extension("hybrid_campaigns", ["hybrid_campaigns.py"], extra_compile_args=["-g0"]),
    Extension("hybrid_merchants", ["hybrid_merchants.py"], extra_compile_args=["-g0"]),
    Extension("hybrid_notes", ["hybrid_notes.py"], extra_compile_args=["-g0"]),
    Extension("kk_struc", ["kk_struc.py"], extra_compile_args=["-g0"]),
    Extension("notes", ["notes.py"], extra_compile_args=["-g0"]),
    Extension("order_items", ["order_items.py"], extra_compile_args=["-g0"]),
    Extension("products", ["products.py"], extra_compile_args=["-g0"]),
    Extension("paysources", ["paysources.py"], extra_compile_args=["-g0"]),
    Extension("purchases", ["purchases.py"], extra_compile_args=["-g0"]),
    Extension("transaction_items", ["transaction_items.py"], extra_compile_args=["-g0"]),
    Extension("transactions", ["transactions.py"], extra_compile_args=["-g0"]),


    #   ... all your modules that need be compiled ...
]
setup(
    name = 'models',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)