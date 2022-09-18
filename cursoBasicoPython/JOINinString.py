#EXTRAER PARTES DEL STRING
s1 = 'test'
s = "testing"


def get_middle(s):
    print(len(s) % 2)
    print(s[len(s)//2], s[len(s)//2-1])
    if len(s)%2 == 0:
        pass


def get_middle1(s):
    long = len(s)
    return "".join((s[long//2-1], s[long//2]) if len(s) % 2 == 0 else s[long//2])


def get_middle2(s):
    index, odd = divmod(len(s), 2)
    print(divmod(len(s), 2))
    print(7//2)
    print(index,odd,len(s))
    return s[index] if odd else s[index - 1:index + 1]

print(get_middle2(s))