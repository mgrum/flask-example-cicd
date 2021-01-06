from setuptools import setup, find_packages
from Cython.Build import cythonize


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flask-example-cicd",
    version="0.1.0",
    author="mgrum",
    author_email="mgrum1994@gmail.com",
    description="This is a simple python flask application to show a CI/CD pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mgrum/flask-example-cicd",
    python_requires='>=3.6',
    ext_modules=cythonize("flaskr/*.pyx"),
    packages=find_packages(),
)
