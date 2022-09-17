from operator import index
from pickletools import string1
import string


text = "The sunset sets at twelve o' clock."


def alphabet_position(text):
    text = text.lower()
    string1 = []
    for letter in text: 
        if letter.isalpha():
            # ord devuelve el unicode para un string el - 96 es el valor para que cuadre con la posicion del alfabeto que es el ord('a')-1
            print(ord(letter) - 96)
        if letter in string.ascii_lowercase:
            string1.append(str(string.ascii_lowercase.index(letter)+1))
    return " ".join(string1)    


s = "The sunset sets at twelve o' clock."
def alphabet_position1(s):
    print(ord("a"))
    return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())
        


print(alphabet_position1(s))


