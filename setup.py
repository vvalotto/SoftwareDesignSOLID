from setuptools import setup

setup(
    name='SenialSOLID',
    version='9.0.0',
    description='SenialSOLID - : Principio DIP',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador', 'configurador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)
