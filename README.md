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

The structure is defined by `struct` class. Also an alias of this class is defined and available as `structure`.

A simple usage code of `ypstruct.struct` follows.

    from ypstruct import *

    p = struct()
    p.x = 3
    p.y = 4
    p.A = p.x * p.y
    print(p)

The output will be:

    struct({'x': 3, 'y': 4, 'A': 12})

Here, after importing the `struct` (and its alias `structure`) from `ypstruct`, an instance of `struct` is created and then fields `x` and `y` are defined. Then, a new field `A` is added to the structure. Finally, the string representation of the `struct` is printed.

In the previous code, you can simply use the following method to create and initialize the structure.

    p = struct(x=3, y=4)
    p.A = p.x * p.y

## Merging Structures

It is possible to merge two `struct` objects. For example let's define two structures as:

    a = struct(x=1, y=2, z=3)
    b = struct(y=5, t=20, u=30)

We can merge these structure using `+` operator:

    c = a + b
    print(c)

The output will be:

    struct({'x': 1, 'y': 5, 'z': 3, 't': 20, 'u': 30})

## Repeating a Structure

Sometimes we need to repeat/replicate a structure. For example, assume that we are going to implement an Evolutionary Algorithm and we defined the individuals as `struct` objects. First we need to create a template:

    empty_individual = struct(pos=None, fval=None)

Then we can initialize the population array using following code:

    pop_size = 10
    pop = empty_individual.repeat(pop_size)

Or simply we can use `*` operator to perform replication:

    pop = empty_individual * pop_size

