


import random




         

def run():
    numero_aleatorio = random.randint(1, 100)
    print(numero_aleatorio)
    
    numero_elegido = 0
    while numero_elegido != numero_aleatorio:
        numero_elegido = input('Elige un numero: ')
        while not numero_elegido.isnumeric():
            numero_elegido = input('Elige un numero: ')
        numero_elegido=int(numero_elegido)
        if numero_elegido > numero_aleatorio:
         print('Te pasate')
        else: 
            print('Te falto')
    print(f'Encontraste el numero y es {numero_aleatorio}')


if __name__ == '__main__':
    print("h"*3)
    run()

    
