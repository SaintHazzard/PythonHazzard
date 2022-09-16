


numbers1 = [1,2,3,4,5]
numbers = [3,4,1,4,1]


def remove_smallest(numbers):
    numbers1 = numbers
    if numbers1:
     
     numbers1.remove(min(numbers))
     return numbers1
    else:
        return []



def remove_smallest1(numbers):
    smallest = numbers.index(min(numbers))
    print(smallest)
    return [i for i in numbers if numbers.index(i) == numbers.index(smallest)]




print(remove_smallest1(numbers))
    
