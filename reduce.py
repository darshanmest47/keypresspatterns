from functools import *

tup=(1,34,56,34,23,101,122)


print(reduce(lambda m,n: m+n,tup))