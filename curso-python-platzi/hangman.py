

import os
from random import randint



def read():
    with open("./curso-python-platzi/data.txt",'r',encoding='utf-8') as f:
        words = [i.replace('\n',"") for i in f]
    return words


def comparar(word_selected,blanks):
    vidas = 10
    w = list(word_selected)
    b = list(blanks)
    while w != b and vidas > 0:
        try:
            usuario = input('Ingrese una letra: \n')
            assert len(usuario) == 1, 'Solo puedes ingresar una letra'
            if not usuario.isalpha():
                raise ValueError
        except ValueError:
            print('Ingresa una jodida letra')
        
        if usuario in w:
            for i,letter in enumerate(w):                
                if letter.lower() in usuario:
                    b[i] = letter
        else:
            vidas -= 1

        print(" ".join(b).upper())
        print('\n')
        print('♥'*vidas)
    if vidas == 0:
        print('Perdiste, estas colgado')
        print("""
         ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''./
        | |/         |/  _  \/
        | |          ||  `/,|
        | |          (\.`_.'
        | |         .-`--'.
        | |        /Y . . Y\.
        | |       // |   | \..
        | |      //  | . |  \..
        | |     ()   |   |   ()
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \.
-------------------------
|  -------------------- |
| |                   | |
: :                   : :  
-------------------------

""")
    else:
        print(""" ::::::::      :::     ::::    :::     :::      ::::::::  ::::::::::: :::::::::: 
:+:    :+:   :+: :+:   :+:+:   :+:   :+: :+:   :+:    :+:     :+:     :+:        
+:+         +:+   +:+  :+:+:+  +:+  +:+   +:+  +:+            +:+     +:+        
:#:        +#++:++#++: +#+ +:+ +#+ +#++:++#++: +#++:++#++     +#+     +#++:++#   
+#+   +#+# +#+     +#+ +#+  +#+#+# +#+     +#+        +#+     +#+     +#+        
#+#    #+# #+#     #+# #+#   #+#+# #+#     #+# #+#    #+#     #+#     #+#        
 ########  ###     ### ###    #### ###     ###  ########      ###     ########## """)
        print(f'Adivinaste la palabra que era {word_selected.capitalize()}')


def normalize(word_selected):  # It removes the accents of a string
    replacements = (("á", "a"), ("é", "e"),  ("í", "i"),  ("ó", "o"), ("ú", "u"),)
    for a, b in replacements:
        word_selected = word_selected.replace(a, b)
    return word_selected

def run():
    os.system('clear')
    words = read()
    word_selected = words[randint(0,len(words))]
    # word_selected = 'plástico'
    word_selected = normalize(word_selected)
    print(word_selected)
    blanks='_'*len(word_selected)
    menu = """
_______________________________________________________________
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"    
---------------------------------------------------------------                                                    
                         |/|
                         |/| /¯)
                         |/|/\/
                         |/|\/
                        (¯¯¯)
                        (¯¯¯)
                        (¯¯¯)
                        (¯¯¯)
                        /¯¯/\.
                       / ,^./\.
                      / /   \/\.
                     / /     \/\.
                    ( (       )/)
                    | |       |/|
                    | |       |/|
                    ( (       )/)
                     \ \     / /
                      \ `---' /
                       `-----'  
______________________________________________________________                       
|     BIENVENIDO AL JUEGO DEL AHORACADO Ó HANGMAN GAME        |
--------------------------------------------------------------
Para comenzar presiona cualquier letra y luego enter
Para salir presiona (Ctrl + C)
______________________________________________________________
"""
    print(menu)
    print(' '.join(blanks))
    comparar(word_selected, blanks)



if __name__ == "__main__":
    run()
    


