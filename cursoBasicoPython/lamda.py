# usando dict llama la operacion con el key y ejecuta la def anonima
def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)


operator = "+"
value1 = 4
value2 = 7


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '*':
        return value1 * value2
    if operator == '-':
        return value1 - value2
    if operator == '/':
        return value1 / value2


print(basic_op(operator, value1, value2))


def unique_in_order(l): return [
    z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
