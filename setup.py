from setuptools import setup

setup(
    name='SenialSOLID',
    version='5.0.0',
    description='SenialSOLID - : Principio LSP - Violación',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador', 'configurador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)
