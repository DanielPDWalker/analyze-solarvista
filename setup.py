from setuptools import setup, find_packages

setup(
    name="matatika-datasets-solarvista",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets for Solarvista",
    packages=find_packages(),
    package_data={"bundle": ["analyze/datasets/tap-solarvista/*.yaml", "orchestrate/tap-solarvista/elt.sh"]},
)
