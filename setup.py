from setuptools import setup, find_packages

setup(
    name='keysafe',
    author='Vitaly Vigasin (ViperVit)',
    author_email='vitolg1@gmail.com',
    license='Apache',
    description='General use library.',
    version='0.1.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test*"])
)
