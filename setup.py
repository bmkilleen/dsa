from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='dsa',
    version='0.1.0',
    description='DSA',
    long_description=readme,
    author='bmk',
    license=license,
    packages=find_packages(exclude=('tests'))
)
