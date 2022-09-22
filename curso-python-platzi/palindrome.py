string = 'ana'

def palindromo(string):
    assert len(string) > 0, 'No puede ser una cadena vacia'
    return string == string[::-1]


print(palindromo(string))