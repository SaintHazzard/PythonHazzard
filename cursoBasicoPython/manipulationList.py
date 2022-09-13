def sum_array1(arr):
    print(sorted(arr)[0:-2])
    print(sorted(arr)[0::-1])
    print(sorted(arr)[-1])
    print(sorted(arr))
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0
