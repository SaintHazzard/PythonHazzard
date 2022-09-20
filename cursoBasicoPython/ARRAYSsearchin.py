s = "bitcoin take over the world maybe who knows perhaps"
# BUSCO LA PALABRA CON MENOS LONGITUD

# min() PUEDE TOMAR ARGUMENTOS AL IGUAL QUE SORTED
def find_short(s):
    # s = s.split()
    print(min(s.split(' '), key=len))
    x = sorted(s, key=len)
    return len(x[0])


def find_short(s):
    return min(len(x) for x in s.split())


def find_short(s):
    return min(map(len, s.split(' ')))


def find_short(s):
    return len(min(s.split(' '), key=len))
print(find_short(s))
