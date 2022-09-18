from functools import reduce
import math
import operator

n = 999


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)])
        print(n)
        i += 1
    return i


print(persistence(n))
