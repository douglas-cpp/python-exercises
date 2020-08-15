"""
An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
Source: https://docs.python.org/3/library/enum.html
"""

from enum import *

class AutoEnumTest(auto):
    A = auto()
    B = auto()

class EnumTest(Enum):
    OWO = 1
    OwO = 2
    oWo = 3

if __name__ == "__main__":
    for owo in EnumTest:
        print(owo)

    for e in AutoEnumTest:
        print(e)

    owo_dict = dict()
    owo_dict[EnumTest.OWO] = 'OWO'
    # Result: {EnumTest.OWO: 'OWO'}
