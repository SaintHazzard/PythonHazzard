bus_stops = [[10,0],[3,5],[5,8]]


def number(bus_stops):
    pplinto = 0
    for stop in bus_stops:
        pplinto += stop[0] - stop[1]
    
    return pplinto


def number1(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


# print(number(bus_stops))


arr1 = [20, 10, -80, 10, 10, 15, 35]
arr = [1, 2, 3, 4, 3, 2, 1]
arr2 = [1, 100, 50, -51, 1, 1]
arr2 = list(range(1, 100))


def find_even_index(arr):
    reverse = arr[::-1]
    # print(reverse)
    # print(arr)
    enu, enum = list(enumerate(arr))
    print(enu, enum)
    for i in range(len(arr)):
        # print(sum(arr[:i:-1]))
        print(i)
        # print((arr[:i]))

        print((arr[:i+1]), reverse[:i+1])
        if sum(arr[:i+1]) == sum(reverse[:i+1]):
            return i
    return -1


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1



lst = [1, 2, 3, 4, 3, 2, 1]
# enumera todos los valores y luego le resta a la suma cada 
def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        
        right_sum -= a
        print(right_sum, 'r')
        if left_sum == right_sum:
            return i
        left_sum += a
        print(left_sum, 'left')
    return -1


print(find_even_index(lst))
