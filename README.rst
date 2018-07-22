#############
Yarpiz Structure (ypstruct)
#############

A simple and easy-to-use C-like structure for Python

---

*************
Installation
*************

Use pip:
::
      pip install ypstruct

if you want to install from source code, you can download from github or simple use:
::
      git clone https://github.com/smkalami/ypstruct

then run:
::
      python setup.py install

*************
Sample Usage
*************
::
      from ypstruct import structure

      if __name__ == "__main__":

            p = structure()
            p.x = 3
            p.y = 4
            p.A = p.x * p.y

            print(p)
