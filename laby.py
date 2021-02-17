import random
from tkinter import *

from Cparam import param
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
parametre = param()
stock1 = []
tabl_canvas = []



def menu():
    menu = Tk()
    menu.geometry(str(parametre.width)+'x'+str(parametre.height))
    canv = Canvas(menu,width=parametre.width,height=parametre.height,bg='black')
    canv.pack()
    play = Button(canv,text='Play',width=20,height=3,bg='black',command=lambda:destroy(menu))
    play.place(x=(parametre.width/2)-100,y=(parametre.height/2)-100)


    btn_param = Button(canv,text="parametre")

    btn_param.place(x=parametre.width-100,y=parametre.height-50)


    menu.mainloop()
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
def fen():
    root = Tk()
    root.geometry(str(parametre.width)+'x'+str(parametre.height))



    generate2()
    generateLaby(2)

    refresh(root)
    game = True
    while(game):









        root.mainloop()
    return root
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
def destroy(fenetre):
    fenetre.destroy()
    jeu()
def jeu():

    generate2()
    generateLaby(2)
    createCheckPoint()
    createBonus()

def refresh(fen):
    x = 0
    y = 0
    labyX = 0
    labyY = 0

    while labyX != 10 and labyY != 10:

        if laby[labyX][labyY] == "*":
            couleur = 'green'
        elif laby[labyX][labyY] == "X":
            couleur = 'red'
        elif laby[labyX][labyY] == "+":
            couleur = 'yellow'
        else:
            couleur = 'cyan'
        canvas2 = Canvas(fen, bg=couleur, width=30, height=30)
        tabl_canvas.append(canvas2)
        canvas2.place(x=x, y=y)

        x += 30
        if x == 300:
            x = 0
            y += 30

        labyX += 1
        if labyX == 10:
            labyY += 1
            labyX = 0



fen()