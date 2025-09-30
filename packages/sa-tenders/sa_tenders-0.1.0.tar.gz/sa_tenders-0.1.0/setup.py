from setuptools import setup, find_packages

#processing the markdown file
with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name= "sa_tenders",
    version= "0.1.0",
    author="Ntuthuko Hlela",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "flatdict", "openpyxl", "requests"],
    description="This library enables developers to download and process data from the South African etenders platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",

)