import string


x = 'man i need a taxi up to ubud'


def high(x):
    alpha = list(string.ascii_lowercase)
    maxsuma = 0
    nums = []
    x = x.split()
    for i in x:
        maxsuma = 0
        for k in i:
            maxsuma += (alpha.index(k))
        nums.append(maxsuma)
    return x[nums.index(max(nums))]


def high2(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


def high3(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))


print(high(x))
