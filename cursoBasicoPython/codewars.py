num = 70304


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

        


print(expanded_form(num))



