n = 3


def tower_builder(n):
    return [('*' * i).center(n * 2 - 1) for i in range(1, n*2 + 1,2)]


print(tower_builder(n))
