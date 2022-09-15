def paperwork(n, m):
    if n > 0 and m > 0:
        return m*n
    else:
        return 0


x = "45385593107843568"


def fake_bin(x):
    a = ''
    for i in x:
        if eval(i) < 5:
            a += "0"
        else:
            a += '1'
    return a


def fake_bin1(x):
    return "".join('0' if i < '5' else '1' for i in x)


print(fake_bin1(x))
