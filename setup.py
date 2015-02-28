from setuptools import setup

setup(
    name='SenialSOLID',
    version='7.0.0',
    description='SenialSOLID - : Principio ISP - Violación',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador', 'configurador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)
