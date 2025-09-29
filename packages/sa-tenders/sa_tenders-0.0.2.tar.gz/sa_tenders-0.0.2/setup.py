from setuptools import setup, find_packages


setup(
    name= "sa_tenders",
    version= "0.0.2",
    author="Ntuthuko Hlela",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "flatdict"],
    description="This library enables developers to download and process data from the South African etenders platform."
)