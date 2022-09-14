


x = int(input('Maximo valor de la potencia \n'))

def potencias_de_2_for(x):
    print('ciclo for')
    for i in range (x):
     print(f'2 elevado a {i} es {2**i}')
    
def potencias_de_2_while(x):
    i=0
    print('ciclo while')
    while i != x:
    
     print(f'2 elevado a {i} es {2**i}')
     i += 1

def tablas_mult_for(x):
    for i in range (x+1):
        print(f'Tabla del {i}')
        for j in range (x+1):
            print(f'{i} * {j} = {i*j}')




# if __name__ == "__main__":
#     tablas_mult_for(x)






