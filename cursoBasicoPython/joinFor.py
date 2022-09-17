numeros = [3,4,8,123,2,3]

# numeros = ", ".join(str(numeros))
numeros1 = ", ".join(str(n) for n in numeros)



# print(numeros, type(numeros))
print(numeros1, type(numeros1))


def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
