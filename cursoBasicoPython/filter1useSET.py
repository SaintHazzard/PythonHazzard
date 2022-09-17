arr = [1, 1, 1, 2, 1, 1,3]

def find_uniq(arr):
    arr = set(arr)
    for i in arr:
         if arr.count(i) == 1:
            return i
    

def find_uniq1(arr):
    i,j = set(arr)
    return i if arr.count(i) == 1 else j


def find_uniq2(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]


print(find_uniq2(arr))
