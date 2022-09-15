seq = [78, 117, 110, 99, 104, 117, 107, 115]
seq1 = seq
elem = 8


def check(seq, elem):
    print(seq is seq1)
    return True if elem in seq else False


x = "45385593107843568"
def fake_bin(x):
    a = ''
    for i in x:
        if eval(i) < 5:
            a+="0"
        else:
            a+='1'
    return a


def fake_bin1(x):
    return "".join('0' if i < '5' else '1' for i in x)


print(fake_bin1(x))
