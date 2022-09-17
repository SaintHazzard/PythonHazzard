import math


def grow(arr):
    return math.prod(arr)


year = 1900

# // las barritas devuelven un int
def century(year):
    print(year//2)
    return math.floor(year/100) if year % 100 == 0 else math.floor(year/100)+1


def century1(year):
    return math.ceil(year / 100)

print(century1(year))
