import random

from pynput.keyboard import Key, Listener

import Character as C












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







stock1 = []
tabl_canvas = []

def ChooseClass(player):

    print('\33[1m' +"Bienvenue, joueur",player, '\33[0m')
    print('\33[35m' +"Tu as le choix entre 3 classes"+ '\33[0m')
    print("1: Bob. Pouvoir: inverse les touches de l'adversaire")
    print("2: José. Pouvoir: construit un mur sur la ligne au dessus de lui pour bloquer son adversaire")
    print("3: Mirabelle. Pouvoir: téléporte l'ennemie sur une case aléatoire")

    input1 = input()

    if(input1 == "1"):
        print("vous avez choisi la classe Bob")
        return "Bob"
    elif (input1 == "2"):
        print("vous avez choisi la classe José")
        return "Jose"
    elif (input1 == "3"):
        print("vous avez choisi la classe Mirabelle")
        return "Mirabelle"




# push = envoyer les infos a l'arduino
def push():
    send = ''
    couleur = ''
    ligne = 0
    colonne = 0
    count = 0
    while ligne != 10 and colonne != 10:

        if laby[ligne][colonne] == "*":
            couleur = '2'  # green
        elif laby[ligne][colonne] == "X":
            couleur = '3'  # red
        elif laby[ligne][colonne] == "+":
            couleur = '4'  # yellow
        elif laby[ligne][colonne] == "=":
            couleur = '5'  # cyan
        elif laby[ligne][colonne] == "+":
            couleur = '6'  #orange
        elif laby[ligne][colonne] == "H":
            couleur = '7'  #violet
        elif laby[ligne][colonne] == "P":
            couleur = '8'  #rose
        elif laby[ligne][colonne] == "V":
            couleur = '9'  #bleu foncé

        ligne += 1
        if ligne == 10:
            colonne += 1
            ligne = 0
        if ligne != 10 and colonne != 10:
            send = send + couleur + ","
        else:
            send = send + couleur
        count += 1
    return send


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


    laby[0][0] = Player1.skin
    laby[9][0] = Player2.skin
    Player1.x = 0
    Player1.y = 0
    Player2.x = 9
    Player2.y = 0



def generate2():

    laby[0][0] = "O"
    laby[9][0] = "O"
    i = 0

    stock1.append(0)
    stock1.append(0)

    while i != 2:  # carre haut gauche

        rand1 = random.randint(0, 4)
        rand2 = random.randint(0, 4)

        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1

    i = 0
    while i != 2:  # bas gauche
        rand1 = random.randint(0, 4)
        rand2 = random.randint(5, 9)
        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1

    i = 0
    while i != 2:  # bas droite
        rand1 = random.randint(5, 9)
        rand2 = random.randint(5, 9)
        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1

    i = 0
    while i != 2:  # haut droit
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
    y0 = stock1[b + 1]

    x1 = stock1[b - 2]
    y1 = stock1[b - 1]

    if x1 > x0:

        count = x0
        while (x1 != count):
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
            y1 -= 1
    else:
        while y1 != count:
            laby[x1][y1] = "*"
            y1 += 1


    if b + 2 <= 19:
        return generateLaby(b + 2)



def display():
    print("")
    print("-----------")
    count = 0
    ligne = 0
    colonne = 0
    while (count != 100):
        if ligne == 10:
            colonne += 1
            ligne = 0
            print()
        print(laby[ligne][colonne] + " ", end='')

        ligne += 1
        count += 1
    return


# met en place l'environnement de jeu
def creation():
    generate2()
    generateLaby(2)
    createCheckPoint()
    createBonus()
    createCharacter()
    display()
    jeu("c")

def finDePartie(player):

    Player1.addPercent(10)
    Player2.addPercent(10)
    Player1.backup_touche()
    Player2.backup_touche()

    if Player1.score == 10:
        print("GAME OVER le joueur 1 a gagné bien joué!")
    elif Player2.score == 10:
        print("GAME OVER le joueur 2 a gagné bien joué!")
    else:
        creation()

def jeu(key):
    game = True


    x1 = Player1.x
    y1 = Player1.y
    x2 = Player2.x
    y2 = Player2.y
    enter = str(key)



    P1 = False
    P2 = False




    if enter.find(Player1.droite) > 0 and x1 < 9:
        print("ici")
        P1 = Player1.move_right(laby)

    if enter.find(Player1.bas) > 0 and y1 < 9:
        P1 = Player1.move_bottom(laby)

    if enter.find(Player1.gauche) > 0 and x1 > 0:
        P1 = Player1.move_left(laby)

    if enter.find(Player1.haut) > 0 and y1 > 0:
        P1 = Player1.move_top(laby)

    if enter.find("r") > 0:
        Player1.use_ultime(laby, Player2)


    if enter.find(Player2.droite) > 0 and x2 < 9:

        P2 = Player2.move_right(laby)

    if enter.find(Player2.bas) > 0 and y2 < 9:

        P2 = Player2.move_bottom(laby)


    if enter.find(Player2.gauche) > 0 and x2 > 0:
        P2 = Player2.move_left(laby)

    if enter.find(Player2.haut) >0 and y2 > 0:
        P2 = Player2.move_top(laby)

    if enter.find("u") > 0:
        Player2.use_ultime(laby,Player1)

    display()
    data = push()
    #arduino.write(data.encode())

    if P1 == True:
        finDePartie(1)
    elif P2 == True:
        finDePartie(2)
    print("le joueur 1 a:", Player1.score," et son ultime est chargé a: ",Player1.pourcentage,"%")
    print("le joueur 2 a:", Player2.score," et son ultime est chargé a: ",Player2.pourcentage,"%")

Player1 = C.Character(ChooseClass(1),"z","d","q","s")
Player2 = C.Character(ChooseClass(2),"o","m","k","l")
creation()


def show(key):
    print('\nYou Entered {0}'.format(key))

    if key == Key.delete:
        # Stop listener
        return False


# Collect all event until released
with Listener(on_press=jeu) as listener:
    listener.join()