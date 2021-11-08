from setuptools import setup, find_packages

setup(
    name="Greetings",
    version="0.1.0",
    packages=find_packages(exclude=["*test"]),
    entry_points={"console_scripts": ["greet = greetings.command:process"]},
)
