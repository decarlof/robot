from setuptools import setup, find_packages

setup(
    name='robot',
    version=open('VERSION').read().strip(),
    author='Francesco De Carlo',
    url='https://github.com/decarlof/robot',
    packages=find_packages(),
    include_package_data = True,
    description='Module to control Universal Robots UR3e at beamline 32-ID',
    zip_safe=False,
)