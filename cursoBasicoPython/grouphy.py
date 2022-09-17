from itertools import groupby

iterable = 'AAAABBBCCDAABBB2234444'
def unique_in_order(iterable):
    for k in groupby(iterable):
        print(k)
    return [k for (k, _) in groupby(iterable)]


print(unique_in_order(iterable))


