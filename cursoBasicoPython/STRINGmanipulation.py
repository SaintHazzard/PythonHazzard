

string3 = 'samurai'
ending4 = 'ra'


def solution(string, ending):
    if ending in string[len(string)-len(ending):]:
        return True
    return False


def solution1(string, ending):
    return ending in string[len(string)-len(ending):]


def solution(string, ending):
    return string.endswith(ending)


# print(solution1(string, ending))

string = "How can mirrors be real if our eyes aren't real"


def to_jaden_case(string):

    string = string.split()
    return " ".join([i.capitalize() for i in string])


# print(to_jaden_case(string))

text = 'Indivisibilities'


def duplicate_count(text):
    text = text.lower()
    contador = 0
    for i, k in enumerate(text):
        if text.count(k) > 1 and k not in text[:i]:
            contador += 1
    return contador


def duplicate_count1(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count


s = 'Indivisibilities'


def duplicate_count2(s):
    # for i in set(s.lower()):
    #     print(i, 'aca')
    # Recorre un nuevo arreglo hecho con set y compara el valor con el array original
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


print(duplicate_count1(text))


def square_digits(num):
    return int("".join([str((int(i)**2)) for i in str(num)]))


# print(square_digits(num))


x = '8 j 8   mBliB8g  imjB8B8  jl  B'


def no_space(x):
    return "".join(i for i in x if i.isdigit() or i.isalpha())


print(no_space(x))
