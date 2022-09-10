def exchanges(pesos, tipo_de_cambio):
    #hago la conversión
    dolares = pesos / tipo_de_cambio
    #redondeo los dólares a dos decimales
    dolares = round(dolares, 3)
    #convierto el float de dolares a un string
    #imprimo el valor de la conversion con f' STRINGS
    print(f'Tienes ${dolares} dolares')


monedas = [{'Pesos colombianos' : 3715.01},
{'Pesos Argentinos': 74.44},
{'Pesos Mexicanos': 21.5}]

# """ """ permite crear strings multilineas
menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Colombianos
2-Pesos Argentinos
3-Pesos Mexicanos

Elige una opción: 

"""

opcion = int(input(menu))


if opcion > 0 and opcion < 4:
    # selecciono el tipo de moneda por la key
    moneda = list(monedas[opcion-1].keys())[0]
    # Establece el tipo de cambio de acuerdo a la moneda seleccionada
    tipo_de_cambio = monedas[opcion-1][moneda]
    # entrada de cuantos pesos
    pesos=float(input(f'Cuantos {moneda} desea cambiar? \n'))
    exchanges(pesos, tipo_de_cambio)
else:
    print(f'Opcion invalida')
    
        





