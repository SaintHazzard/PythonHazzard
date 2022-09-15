from curses.ascii import isdigit




primos = []
noprimos = []

# valida solo un numero excluyendo el 1 y el mismo, lo que significa que si encuentra modulo = 0 no es primo
def is_prime(n): 
    for i in range(2, n):
        
        if (n % i) == 0:
          return f'{n} no es primo'
    return f'{n} si es primo'  
            

# valida el rango incluido el 1 y el numero en si mismo, por lo que si es primo el maximo valor a tomar debe ser 2 a diferencia de los demas
nIN = input('Ingrese el rango final de primos a consultar: ')
while not nIN.isnumeric():
    nIN = input('Ingrese el rango final de primos a consultar: ')
nIN = int(nIN)


def is_prime_range(nIN):

    primo = 0
    for i in range(1,nIN+1):
        for k in range(1,i+1):
            if i % k == 0:
                primo += 1
        if primo == 2:
         primos.append(i)
        else: 
            noprimos.append(i) 
        primo = 0
    return f'Numeros primos del rango {primos} \nNumeros no primos {noprimos}'


 


print(is_prime_range(nIN))
    
        
