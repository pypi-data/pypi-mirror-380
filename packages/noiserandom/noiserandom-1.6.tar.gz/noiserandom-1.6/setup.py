from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    description = readme.read()

setup(
    name="noiserandom",
    author="Andreas Karageorgos",
    version="1.6",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "gmpy2"
    ],
    license="MIT",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndreasKarageorgos/noiserandom"
    
)