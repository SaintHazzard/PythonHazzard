
def series_sum1(n):
    # return str(round(sum([round(1/i, 2) for i in range(1, 3*n, 3)]),2))
    print(round(1.0, 5))
    return str(float(round(sum([1/(1+i*3) for i in range(n)]), 2)))


def series_sum(n):
    return '{:.2f}'.format(sum((1/i) for i in range(1, n*3, 3)))


# print(series_sum(1))
# print(series_sum(2))
# print(series_sum(3))
# print(series_sum(5))
# print(series_sum(24))





array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]


def count_sheeps(array1):
  return array1.count(True)


print(count_sheeps(array1))
