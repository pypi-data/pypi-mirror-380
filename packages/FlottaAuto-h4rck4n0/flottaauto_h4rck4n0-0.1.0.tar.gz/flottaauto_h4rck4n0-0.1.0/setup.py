from setuptools import setup, find_packages

#Legge il contenuto del file README.md
with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name="FlottaAuto-h4rck4n0",
	version="0.1.0",
	packages=find_packages(),	
	install_requires=[],
    author="h4rck4n0",
	description="Gestione Flotta Auto - progetto del corso Python di Hacknow - roby7979",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="",
)
