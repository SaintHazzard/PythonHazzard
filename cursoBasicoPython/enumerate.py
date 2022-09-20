
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


def accum2(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))


def expanded_form(num):
 digits = str(num)  # convert number to string
 output = []
 for i, digit in enumerate(digits):
   output.append("(" + digit + "x10^" + str(len(digits)-i-1) + ")")
 return " + ".join(output)


def expanded_form(num):
    digits = str(num)
    out = []
    for pos, val in enumerate(digits[::-1]):
        if str(val) > '0':
            out.append(eval(val)*10**pos)
    return " + ".join(str(i) for i in out[::-1] if str(i) > '0')


# print(expanded_form(num))
