from setuptools import setup,find_packages
from typing import List
from pathlib import Path


setup(
    name = "brain_tumor_classification",
    version= "0.0.0",
    author= "Ankit M Zanzmera",
    author_email= "22msrds052@jainuniversity.ac.in",
    url= "https://github.com/Ankitzanzmera/chicken_disease_classification",
    packages= find_packages(where="src"),
    package_dir={"":"src"}
)
