arr = []
# contador de positivos y sumador de negativos


def count_positives_sum_negatives(arr):
    count = 0
    suma = 0
    if len(arr) == 0:
        return []
    for value in arr:
        if value > 0:
            count += 1
        if value < 0:
            suma += value
    return [count, suma]


def count_positives_sum_negatives1(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

print(count_positives_sum_negatives(arr))
