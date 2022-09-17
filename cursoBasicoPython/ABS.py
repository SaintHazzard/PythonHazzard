

# retorna numero negativo siempre codewars
def make_negative(number):
    return -abs(number)


def make_negative(number):
    return -number if number > 0 else number
