n = 12

primos = []
noprimos = []

# valida solo un numero
def is_prime(n): 
    for i in range(2, n):
        
        if (n % i) == 0:
          return f'{n} no es primo'
    return f'{n} si es primo'  
            



def is_prime_range(n):
    primo = 0
    for i in range(2,n+1):
        for k in range(2,i+1):
            if i % k == 0:
                primo += 1
        if primo == 2:
            primos.append(i)
            break
        elif primo != 2:
            noprimos.append(i) 
            break 
        primo = 0
    return f'Numeros primos del rango {primos} \nNumeros no primos {noprimos}'


 


print(is_prime_range(n))
    
        
