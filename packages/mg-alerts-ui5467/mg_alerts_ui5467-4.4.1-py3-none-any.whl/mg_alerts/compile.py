
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("process_manager", ["process_manager.py"], extra_compile_args=["-g0"]),
    Extension("alert_models", ["alert_models.py"], extra_compile_args=["-g0"]),

]
setup(
    name='alerts',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)