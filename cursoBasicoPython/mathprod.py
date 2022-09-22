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


n = 999


def persistence(n):
    newN = [int(i) for i in str(n)]
    if len(newN) == 1:
        return 0
    ciclos = 0
    while len(newN) != 1:
        print(newN)
        if len(newN) == 1:
            return ciclos
        else:

            val = math.prod(newN)
            print(val)
            newN = [int(i) for i in str(val)]
            ciclos += 1
    return ciclos


print(persistence(n))
