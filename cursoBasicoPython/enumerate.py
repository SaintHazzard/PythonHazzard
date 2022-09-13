
arr = [1, 2, 3, 4, 6, 7, 8]
def first_non_consecutive(arr):
    for x in range(len(arr)):
        if ((arr[x] + 1) != arr[x+1]):
            return arr[x+1]


def first_non_consecutive1(arr):
    if not arr:
        return 0
    for a,b in enumerate(arr[:-1]):
        print(a,b)
        if b + 1 != arr[a + 1]:
            return arr[a + 1]

print(first_non_consecutive1(arr))