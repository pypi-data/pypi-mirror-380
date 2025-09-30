from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("tg_config", ["tg_config.py"], extra_compile_args=["-g0"]),
    Extension("tg_alerts", ["tg_alerts.py"], extra_compile_args=["-g0"]),
    Extension("tg_base", ["tg_base.py"], extra_compile_args=["-g0"]),
]
setup(
    name='telegram',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)