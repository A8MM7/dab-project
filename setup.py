from setuptools import setup, find_packages

setup(
    name='dab_project',
    version='0.0.1',
    description="This contains the code in the ./src directory, which is used in the Databricks notebooks.",
    author='JJ Envie',
    packages=find_packages(where='./src'),
    package_dir={'': './src'},
    install_requires=[
        'setuptools'
    ]
)