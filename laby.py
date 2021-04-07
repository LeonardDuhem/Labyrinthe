import random
import keyboard
import time
import jose as J


laby = [["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"]]



Player1 = J.jose()


stock1 = []
tabl_canvas = []

#push = envoyer les infos a l'arduino
def push():
    send = ''
    couleur = ''
    ligne = 0
    colonne = 0
    count = 0
    while ligne != 10 and colonne != 10:

        if laby[ligne][colonne] == "*":
            couleur = 'green'
        elif laby[ligne][colonne] == "X":
            couleur = 'red'
        elif laby[ligne][colonne] == "+":
            couleur = 'yellow'
        else:
            couleur = 'cyan'

        ligne += 1
        if ligne == 10:
            colonne += 1
            ligne = 0

        send = send + str(count) + ':' +couleur + ","
        count += 1
    print(send)



def createCheckPoint():
    rand1 = random.randint(0, 9)
    rand2 = random.randint(5, 9)
    if laby[rand1][rand2] == '*':
        laby[rand1][rand2] = '+'
    else:
        return createCheckPoint()



def createBonus():
    rand1 = random.randint(0, 9)
    rand2 = random.randint(5, 9)
    if laby[rand1][rand2] == '*':
        laby[rand1][rand2] = '='
    else:
        return createBonus()

def createCharacter():
    laby[0][0] = "H"









def generate2():
    count = 0
    ligne = 0
    colonne = 0

    laby[0][0] = "O"
    laby[9][0] = "O"
    i = 0

    stock1.append(0)
    stock1.append(0)



    while i != 2:                       #carre haut gauche

        rand1 = random.randint(0, 4)
        rand2 = random.randint(0, 4)

        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i+=1

    i = 0
    while i != 2:                   # bas gauche
        rand1 = random.randint(0, 4)
        rand2 = random.randint(5, 9)
        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1

    i = 0
    while i != 2:                      #bas droite
        rand1 = random.randint(5, 9)
        rand2 = random.randint(5, 9)
        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1

    i = 0
    while i != 2:                       #haut droit
        rand1 = random.randint(5, 9)
        rand2 = random.randint(0, 4)
        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1



    stock1.append(9)
    stock1.append(0)

def generateLaby(b):

    laby[0][0] = "*"
    laby[9][0] = "*"

    x0 = stock1[b]
    y0 = stock1[b+1]

    x1 = stock1[b-2]
    y1 = stock1[b-1]

    if x1>x0:

        count = x0
        while(x1 != count):

            laby[x1][y1] = '*'
            x1 -= 1
        count = y0

    else:

        count = x0
        while (x1 != count):

            laby[x1][y1] = '*'
            x1 += 1
        count = y0

    if(y1 > y0):

        while y1 != count:
            laby[x1][y1] = "*"
            y1-=1
    else:
        while y1 != count:
            laby[x1][y1] = "*"
            y1 += 1

    if b+2 <= 19:

        return generateLaby(b+2)
def display():
    print("")
    print("-----------")
    count = 0
    ligne = 0
    colonne = 0
    while(count != 100):
        if ligne == 10:
            colonne += 1
            ligne = 0
            print()
        print(laby[ligne][colonne]+" ", end='')

        ligne+=1
        count+=1
    return


#met en place l'environnement de jeu
def creation():

    generate2()
    generateLaby(2)
    createCheckPoint()
    createBonus()
    createCharacter()
    display()
    jeu()

def jeu():
    game = True

    while game == True:
        x1 = Player1.x
        y1 = Player1.y
        enter = input('')

        if enter == 'd':
            if laby[x1+1][y1] == "*" and y1 < 9:
                laby[ x1+ 1 ][y1] = "H"
                laby[x1][y1] = "*"
                Player1.x = x1+1
                Player1.y = y1
            elif laby[x1+1][y1] == "+":
                Player1.score += 1

                return creation()

        if enter == 's' and y1 < 9:
            if laby[x1][y1+1] == "*":
                laby[x1][y1+1] = "H"
                laby[x1][y1] = "*"
                Player1.x = x1
                Player1.y = y1 + 1
            elif laby[x1][y1 + 1] == "+":
                Player1.score += 1
                return creation()




        if enter == 'q' and x1 > 0:
            if laby[x1-1][y1] == "*":
                laby[x1-1][y1] = "H"
                laby[x1][y1] = "*"
                Player1.x = x1 - 1
                Player1.y = y1
            elif laby[x1-1][y1] == "+":
                Player1.score += 1
                return creation()


        if enter == 'z' and y1 > 0:
            if laby[x1][y1-1] == "*":
                laby[x1][y1-1] = "H"
                laby[x1][y1] = "*"
                Player1.x = x1
                Player1.y = y1 -1
            elif laby[x1][y1-1] == "+":
                Player1.score+=1
                return creation()
        display()


creation()
