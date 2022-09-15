words = ['hello']

def smash(words):
    print(len(words))
    
    return " ".join(words) if len(words) >= 1 else ""

# envio los strings multiplicados a una list
def accum(s):
    string = []
    for i in range(len(s)):

        ns = s[i] * (i+1)
        string.append(ns.capitalize())

    return "-".join(string)

# enumerate() devuelve una tupla con posicion enumerada desde 1 y el valor, luego coloca la letra mayuscula y suma en un ciclo la letra lower() la enumeracion devuelva por enumerate
def accum1(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def accum2(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))


print(smash (words))



nombres = ['Juan','Oliva','Daniela','Edward']


print('contenido',nombres)

formato = ', '.join(nombres)

print(formato)
