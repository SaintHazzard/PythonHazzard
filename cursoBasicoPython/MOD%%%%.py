flower1 = 413
flower2 = 886


def lovefunc(flower1, flower2):
    return (flower1 % 2 == 0 or flower2 % 2 == 0) and (flower1 % 2 == 1 or flower2 % 2 == 1)


def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2


print(lovefunc(flower1, flower2))
