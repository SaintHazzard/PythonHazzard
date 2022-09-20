import string


message = 'test'
def rot13(message):
    for i in message:
        x = (ord(i)+13)
        y = chr(4)
        print(x,y)