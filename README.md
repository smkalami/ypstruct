# Yarpiz Structure (ypstruct)

A simple and easy-to-use MATLAB-like structure type for Python


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


## `dict` vs. `struct`

Actually `struct` is a subclass of built-in dictionary type `dict`, and it can be converted to or created from `dict` objects.

You can convert `dict` objects to `struct` as follows:

    my_dict = {'x':3, 'y':4}
    p = struct(my_dict)

Also, `struct` object can be converted to `dict` as well:

    p = struct(x=3, y=4)
    p.z = 12
    my_dict = dict(p)
    print(my_dict)

The output will be this:

    {'x': 3, 'y': 4, 'z': 12}


## Merging Structures

It is possible to merge two `struct` objects. For example let's define two structures as:

    a = struct(x=1, y=2, z=3)
    b = struct(y=5, t=20, u=30)

We can merge these structure using `+` operator:

    c = a + b
    print(c)

The output will be:

    struct({'x': 1, 'y': 5, 'z': 3, 't': 20, 'u': 30})


## List of the Methods

In this part, we are going to discuss the methods implemented and available in `struct` class and its alias `structure`. You can use these methods with any instance of `struct` class. Additionally, because the `struct` class is a subclass of `dict`, all of the methods defined in the `dict` class are available too.


### `fields()` Method

The `fields()` method returns a `list` of fields defined in structure. An example usage follows:

    p = struct(x=3, y=4)
    print(p.fields())

The output will be:

    ['x', 'y']


### `add_field()` Method

A new field can be added using `add_field()` method. This method accepts two input arguments: field name and its value. The value is optional and if it is ignored, then value is assumed to be `None`. A sample code follows:

    p = struct(x=3, y=4)
    p.add_field('z', 12)
    p.add_field('L')
    print(p)

The output of this code will be:

    struct({'x': 3, 'y': 4, 'z': 12, 'L': None})

Instead of using the `add_field()` method, it is possible to use `.` and `=` operators. For example, the above-mentioned code can be simplified as this:

    p = struct(x=3, y=4)
    p.z = 12
    p.L = None
    print(p)

The result will be the same.


### `remove_field()` Method

A field can be removed from a `struct` object using `remove_field()` method. This method gets a field name and it removes (deletes) the specified field. An example is given below:

    p = struct(x=3, y=4, z=12)
    print('Before remove_field: {}'.format(p))
    p.remove_field('z')
    print('After remove_field: {}'.format(p))
    
The output will be this:

    Before remove_field: struct({'x': 3, 'y': 4, 'z': 12})
    After remove_field: struct({'x': 3, 'y': 4})


### `repeat()` Method: Repeating a Structure

Sometimes we need to repeat/replicate a structure. For example, assume that we are going to implement an Evolutionary Algorithm and we defined the individuals as `struct` objects. First we need to create a template:

    empty_individual = struct(pos=None, fval=None)

Then we can initialize the population array using following code:

    pop_size = 10
    pop = empty_individual.repeat(pop_size)

This code uses the `repeat()` method to initialize a list of distinct `struct` objects with the same data fields. Instead of using `repeat()` method, simply we can use `*` operator to perform replication:

    pop = empty_individual * pop_size


### `copy()` and `deepcopy()` Methods

The `struct` is a reference type. To have a copy of a `struct` object, you cannot simply use assignment operator. To create copies of structure objects, two methods are implemented in `struct` class: `copy()` and `deepcopy()`. The first one gives us a shallow copy of the `struct` object. But using `deepcopy()`, as the name of the method says, we can create deep copies of structure objects.
