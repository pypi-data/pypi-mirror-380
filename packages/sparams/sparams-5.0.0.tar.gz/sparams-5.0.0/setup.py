from setuptools import setup, find_packages

setup(
    name='sparams',
    version='5.0.0',
    description='A simple config watcher ',
    author='PAT',
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'pyyaml',
        'numpy',  
    ],
    python_requires='>=3.8',
    long_description = open("README", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)