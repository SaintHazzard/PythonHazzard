from dataclasses import replace
import re
from curses.ascii import isdigit
from numbers import Number
from re import I


s = "ooxXm"
def xo(s):
    s= s.lower()
    return True if s.count('o') == s.count('x') else False

# print(xo(s))


sentence = "is2 Thi1s T4est 3a"
# print(sentence.split(),'split solo')
# print(sorted(sentence.split()),'sorted')
# print(sorted(sentence.split(), key=lambda w: sorted(w)))

# def order(sentence):
#   senten = sentence.split()

#   for word in senten:
#     for letter in word:
#         if letter.isdigit():
#     # print(senten)



def order1(sentence):
    sentence = sorted(sentence.split())
    order_sentence = []
    for word in range(len(sentence)):
        for letter in word:
            pass


    return sentence


def order2(sentence):
    sentence=sentence.split()
    order_sentence = []
    for i in range(1,10):
        for w in sentence:
            if str(i) in w:
                order_sentence.append(w)
    return " ".join(order_sentence)


def order(sentence):
  return " ".join(sorted(sentence.split(), key=min))


# print(order2(sentence))

'elbuod decaps sdrow'
text = 'elbuod  decaps  sdrow'
text1 = "This is an example!"
def reverse_words(text):
    if "  " in text:
        text = text.split()
        return "  ".join(i[::-1] for i in text)
    else:
        text = text.split()
        return " ".join(i[::-1] for i in text)


def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)


print(reverse_words(text))





