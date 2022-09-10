def es_palindromo(palabra):
    palabra = palabra.replace(' ','').lower()
    if palabra == palabra[::-1]:
            print(f'{palabra} es palidromo')
    else:
             print(f'No es palidromo')

def ejecutar():
     palabra = input(f'Indique una frase o una palabra para verificar si es un palidromo: \n')
     es_palindromo(palabra)
   


if __name__ == "__main__":
    ejecutar()