"""
import pack.one

# Whenever we will import a file form package, __init__.py will be executed

print()

pack.one.fun()
cRef = pack.one.CA()
"""

"""
import pack.one as o

print()

o.fun()
cRef = o.CA()
"""

# from pack.one import fun, CA
from pack.one import *

print()

fun()
cRef = CA()