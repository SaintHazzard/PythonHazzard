
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


a = [1, 2, 2]
b = [1]

# filtra los elementos diferentes entre 2 arrays
def array_diff(a, b):
    return [i for i in a if i not in b]


print(array_diff(a,b))
