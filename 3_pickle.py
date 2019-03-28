"""
This is basic examples of using pickle to serialize data
https://docs.python.org/3/library/pickle.html
"""

import pickle

# can be pickled are:
# None, True, and False
# integers, floating point numbers, complex numbers
# strings, bytes, bytearrays
# tuples, lists, sets, and dictionaries containing only picklable objects
# functions defined at the top level of a module (using def, not lambda)
# built-in functions defined at the top level of a module
# classes that are defined at the top level of a module
# instances of such classes whose __dict__ or the result of calling __
# getstate__() is picklable (see section Pickling Class Instances for details).


class Foo:
  attr = 'A class attribute'


picklestring = pickle.dumps(Foo)

Foo = pickle.load(picklestring)