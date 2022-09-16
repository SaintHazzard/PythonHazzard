from re import S


words = ['hello', 'world', 'this', 'is', 'great']


def smash(words):
    sentence = ''
    for x in range(0,len(words)):
        
        sentence += words[x]
    
        if x < 2:
            sentence += " "
    return sentence

    
    
    
    
# print(smash(words))



