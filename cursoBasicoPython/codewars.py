from re import I


iterable = 'AAAABBBCCDAABBB'


def unique_in_order(iterable):
    return [iterable[i] if iterable[i] != iterable[i+1] else None for i in iterable]


def unique_in_order1(iterable):
    result = []
    prev = None
    print(iterable[:])
    for char in iterable[:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


def unique_in_order2(iterable):
    newList = []
    for item in iterable:
        print(len(newList))
        if not len(newList) or item != newList[len(newList) - 1]:
            newList.append(item)
    return newList

print(unique_in_order2(iterable))








