from setuptools import setup, find_packages

setup(
    name="theMostPowerfulCatEver",
    version="0.5",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "meow=theMostPowerfulCatEver:meow",
        ]
    }
)