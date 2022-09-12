from email.mime import base


def es_palindromo(palabra):
    palabra_base = palabra
    palabra = palabra.replace(' ','').lower()
    if palabra == palabra[::-1]:
            print(f'\n {palabra_base} es palidromo')
    else:
             print(f'No es palidromo')

def run():
     palabra = input(f'Indique una frase o una palabra para verificar si es un palidromo: \n')
     es_palindromo(palabra)
   


if __name__ == "__main__":
    run() 