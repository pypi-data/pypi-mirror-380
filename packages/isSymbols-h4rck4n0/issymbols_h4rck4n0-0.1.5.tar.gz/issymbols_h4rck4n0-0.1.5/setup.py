from setuptools import setup, find_packages

#Legge il contenuto del file README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="isSymbols-h4rck4n0",
    version="0.1.5",
    packages=find_packages(),   
    install_requires=[],
    author="h4rck4n0",
    description="script che controlla se ci sono simboli in una stringa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
)
