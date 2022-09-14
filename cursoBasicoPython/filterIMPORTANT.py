
l = [1, 2, 'a', 'b']

def filter_list(l):
    return list(filter(lambda tipo: type(tipo) == int , l))


print(filter_list(l))



x = ["Ryan", "Kieran", "Mark"]

def friend(x):

   return list(filter(lambda friend: len(friend) == 4, x))

print(friend(x))


def friend(x):
    return [f for f in x if len(f) == 4]
