
l = [1, 2, 'a', 'b']

def filter_list(l):
    return list(filter(lambda tipo: type(tipo) == int , l))




print(filter_list(l))



