def get_sum(a, b):
    s = 0
    if a == b:
        return a or b
    for i in range(min(a, b), max(a, b)+1):
        s += i
    return s

# AMBAS FUNCIONAN BIEN


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


print(get_sum(1, 5))

arr = [1,-4,7,12]
def positive_sum(arr):
    return sum(i for i in arr if i > 0)


print(positive_sum(arr))
