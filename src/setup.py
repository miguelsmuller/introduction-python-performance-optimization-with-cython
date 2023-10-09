from distutils.core import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize(["src/module_2.pyx"]))
