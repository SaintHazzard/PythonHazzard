words = ['hello']

def smash(words):
    print(len(words))
    
    return " ".join(words) if len(words) >= 1 else ""


print(smash (words))



nombres = ['Juan','Oliva','Daniela','Edward']


print('contenido',nombres)

formato = ', '.join(nombres)

print(formato)
