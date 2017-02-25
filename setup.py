from setuptools import setup
from setuptools import find_packages


setup(name='pyminos',
      version='0.2.0',
      description='Neural nets hyper parameters & architecture search with genetic algorithms',
      keywords=['keras', 'genetic algorithm', 'neural network', 'deep learning'],
      author='Julien Roch',
      author_email='julien.roch@akalea.com',
      url='https://github.com/guybedo/minos',
      license='Apache',
      setup_requires=[
          'numpy>=1.12'],
      install_requires=[
          'numpy>=1.12',
          'keras',
          'deap>=1.0.2'],
      extras_require={
          'h5py': ['h5py'],
          'tests': ['pytest',
                    'pytest-cov',
                    'pytest-pep8',
                    'pytest-xdist',
                    'python-coveralls',
                    'coverage==3.7.1'],
      },
      packages=find_packages())
