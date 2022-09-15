


print(check(seq, elem))
    


numbers = [5, 8, 12, 18, 22]
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    # print(numbers)
    return numbers[0] + numbers[1]


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


# print(sum_two_smallest_numbers(numbers))