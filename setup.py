from setuptools import setup, find_packages

setup(
    name='SmartFarmDataMartAPI',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here, for example:
        'requests',
        'pyyaml',
    ],
    author='Junho Kim',
    author_email='zz1236zz@gmail.com',
    description='An API for Smart Farm Data Management and Visualization',
    keywords='smart farm api data agriculture',
)
