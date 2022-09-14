def get_count(sentence):
    contador = 0
    for letra in sentence:
        if letra.lower() in 'aeiou':
            contador += 1

    return contador




def digitize(n):
    return [int(x) for x in str(n)[::-1]]
    
    
    
    n = str(n)
    print(list(n[::-1]))
    for val in n:
        list(val)   

    print(digitize(n))
