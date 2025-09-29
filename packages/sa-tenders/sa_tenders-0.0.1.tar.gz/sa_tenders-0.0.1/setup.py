from setuptools import setup, find_packages


setup(
    name= "sa_tenders",
    version= "0.0.1",
    author="Ntuthuko Hlela",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "flatdict"]

)