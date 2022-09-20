n = 3


def tower_builder(n):
    return [('*' * i).center(n * 2 - 1) for i in range(1, n*2 + 1,2)]


print(tower_builder(n))


def open_or_senior(data):
    lisort = []
    for age, handi in data:
        if age >= 55 and handi > 7:
            lisort.append('Senior')
        else:
            lisort.append('Open')
    return lisort


d = 8


def rental_car_cost(d):
    cost = 0
    for i in range(d):
        cost += 40
    if i > 5:
        cost -= 50
    if i >= 3:
        cost -= 20
    return cost


# print(rental_car_cost(d))
