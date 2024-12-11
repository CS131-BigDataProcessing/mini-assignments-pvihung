from setuptools import setup, find_packages

setup(
    name='crime_test',
    version='1.0.0',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['pandas>=1.1.0'],
    author='Hung Pham',
    author_email='hung.v.pham@sjsu.edu',
)

