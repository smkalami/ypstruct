# Yarpiz Structure (ypstruct)

A simple and easy-to-use C/C++/MATLAB-like structure type for Python


## Installation

You can use pip to install `ypstruct`:

    pip install ypstruct

If you want to install from source code, you can download from github or simply use:

    git clone https://github.com/smkalami/ypstruct

and then, run this:

    python setup.py install


## Sample Usage

A simple code follows.

    from ypstruct import structure

    p = structure()
    p.x = 3
    p.y = 4
    p.A = p.x * p.y
    print(p)

Here, after importing the `structure` from `ypstruct`, an instance of `structure` is created and then fields `x` and `y` are defined. Then, a new field `A` is added to the structure. Finally, the string representation of the `structure` is printed.

In the previous code, you can simply use the following method to create and initialize the structure.

    p = structure(x=3, y=4)
    p.A = p.x * p.y

.