import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "ypstruct",
    version = "0.0.2",
    author = "Mostapha Kalami Heris",
    author_email = "sm.kalami@gmail.com",
    description = "A simple and easy-to-use C/C++/MATLAB-like structure type for Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/smkalami/ypstruct",
    packages = ["ypstruct"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)