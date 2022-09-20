array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]


def comp(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []


def comp(array1, array2):
    try:
        return sorted([i*i for i in array1]) == sorted(array2)
    except:
        return False


print(comp(array1, array2))
