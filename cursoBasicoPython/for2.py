n = 3


def tower_builder(n):
    return [('*' * i).center(n * 2 - 1) for i in range(1, n*2 + 1,2)]


print(tower_builder(n))


def open_or_senior(data):
    lisord = []
    for age, handi in data:
        if age >= 55 and handi > 7:
            lisord.append('Senior')
        else:
            lisord.append('Open')
    return lisord
