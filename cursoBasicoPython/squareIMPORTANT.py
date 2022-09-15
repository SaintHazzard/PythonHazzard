


import math
n = -1


def is_square(n):
    if n >= 0:
        return math.sqrt(n).is_integer()
    return False


def is_square1(n):
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False


print(is_square(n))

a = 3
b = 2
c = 4


def is_triangle(a, b, c):
    if a == b or a == c or b == c and a - b < 2 or a - c < 2:
        return True
    else:
        return False


def is_triangle1(a, b, c):
    print(sorted([a, b, c]))
    a, b, c = sorted([a, b, c])
    print(a)
    return a + b > c


# print(is_triangle1(a, b, c))


sq = 121


def find_next_square(sq):
    if sq % sq**0.5 == 0: #encuentra el valor sin residuo para que sea una potencia entera **0.5 es raiz cuadrada
        print(pow((sqrt(sq)+1), 2), 'normal') # devuelve el valor sq y le suba 1 para hayar el cuadrado entero siguient
        print(type(print(pow((sqrt(sq)+1), 2))), 'tipo')


# find_next_square(sq)


