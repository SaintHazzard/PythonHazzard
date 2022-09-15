# dividir el string por el espacio y capitalizar las primeras letras de cada palabra
name = "Sam Harris"


def abbrev_name(name):
    name.capitalize()
    return ".".join(name[0] + name[name.index(i)+1] for i in name if i == " ")


def abbrev_name1(name):
    return '.'.join(i[0] for i in name.split()).upper()


def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

print(abbrev_name(name))
