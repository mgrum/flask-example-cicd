from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name="flask example app",
    ext_modules=cythonize("flaskr/prime_cython.pyx"),
    packages=find_packages(),
)
