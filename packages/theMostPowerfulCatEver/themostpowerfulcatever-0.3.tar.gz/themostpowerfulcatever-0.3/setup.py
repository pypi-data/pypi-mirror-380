from setuptools import setup, find_packages

setup(
    name="theMostPowerfulCatEver",
    version="0.3",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "meow=Cat:meow",
        ]
    }
)