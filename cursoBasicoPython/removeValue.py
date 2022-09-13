arr = [6, 2, 1, 8, 10]
def sum_array(arr):
    if arr is None or len(arr) < 2:
        return 0
    arr.remove(max(arr)) and arr.remove(min(arr))
    return sum(arr)
            

def sum_array1(arr):
    print(sorted(arr)[1:-1])
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0



print(sum_array1(arr))