import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ypstruct",
    version="0.0.1",
    author="Mostapha Kalami Heris",
    author_email="sm.kalami@gmail.com",
    description="A simple and easy-to-use C-like structure for Python",
    long_description=long_description,
    url="https://github.com/smkalami/ypstruct",
    packages=['ypstruct'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)