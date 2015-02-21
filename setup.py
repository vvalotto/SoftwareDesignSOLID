from setuptools import setup, find_packages
from codecs import open

setup(
    name='SenialSOLID',
    version='2.0.0',
    description='SenialSOLID: Principio de Responsabilidad Unica',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=['senial_SOLID'],
    py_modules=['lanzador'],
    entry_points = {'console_scripts':
                    'lanzador = lanzador:Lanzador.ejecutar'}
)