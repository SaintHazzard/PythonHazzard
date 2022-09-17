
from collections import Counter
import string


string1 = 'aba'


# count() cuenta cuantas veces aparece un valor o caracter
def is_isogram(string):
    if not string:
        return True
    else:
        string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True
        

# set crea un nuevo array sin los valores repetidos
def is_isogram1(string):
    # print(set(string.lower()))
    # print(len(set(string.lower())))
    return len(string) == len(set(string.lower()))

# print(is_isogram1(string))


s = "The quick brown fox jumps over the lazy dog."


def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

# Este funciona correctamente
def is_pangram1(s):
    set = []
    s = s.lower()
    for i in s:
      if i.isalpha():
        if i not in set:
          set.append(i)
    return len(set) == 26


def is_pangram(s):
    s = s.lower()
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True


print(is_pangram(s))


word = "Dind"
# funciona correctamente


def duplicate_encode(word):
    s = ''
    word = word.lower()
    print(word)
    for i in word:
        if word.count(i) == 1:
            s += "("
        else:
            s += ")"

    return s


# print(duplicate_encode(word))


def duplicate_encode1(word):
    word = word.lower()
    counter = Counter(word)
    print(counter)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)


print(duplicate_encode1(word))
