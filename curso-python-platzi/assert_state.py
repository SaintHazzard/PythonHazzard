def divisors(num):
    
    return [i for i in range(1,num+1) if num % i == 0]


def run():
    num = input('Ingresa un numero entero positivo: ')
    assert num.isdigit() and num > 0, 'Ingresa un numero'
    num = int(num)
    print(divisors(num))


if __name__ == "__main__":
    run()