from setuptools import setup, find_packages

setup(
      name = 'syntheticRNASeq',
      version = '0.0.1',
      packages = find_packages('syntheticRNASeq'),
      install_requires = ['numpy>=1.26.4',
                          'pandas>=2.2.2'
                          ]
      )

