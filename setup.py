from distutils.core import setup
from setuptools.extension import Extension
from setuptools import find_packages


setup(name='thriftpool',
       version = '1.0',
       description = 'thrift connection pool',
       author="Adrian Muraru",
       author_email="amuraru@adobe.com",
       packages=find_packages('src'),
       package_dir={'': 'src'},
       include_package_data=True,
       install_requires=[
        'gevent >= 0.13'
       ])
