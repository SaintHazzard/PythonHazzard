
string = 'aba'


# count() cuenta cuantas veces aparece un valor o caracter
def is_isogram(string):
    if not string:
        return True
    else:
        string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True
        

# set crea un nuevo array sin los valores repetidos
def is_isogram1(string):
    print(set(string.lower()))
    print(len(set(string.lower())))
    return len(string) == len(set(string.lower()))

print(is_isogram1(string))