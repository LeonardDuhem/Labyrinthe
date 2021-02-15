import random

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

def generate2():
    count = 0
    ligne = 0
    colonne = 0

    laby[0][0] = "O"
    laby[9][0] = "O"
    i = 0
    while i != 2:                       #carre haut gauche

        rand1 = random.randint(0, 4)
        rand2 = random.randint(0, 4)


        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i+=1
    i = 0

    while i != 2:
        rand1 = random.randint(5, 9)
        rand2 = random.randint(5, 9)
        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1

    i = 0
    while i != 2:
        rand1 = random.randint(0, 4)
        rand2 = random.randint(5, 9)
        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1
    i = 0
    while i != 2:
        rand1 = random.randint(5, 9)
        rand2 = random.randint(0, 4)
        if laby[rand1][rand2] != "*":
            laby[rand1][rand2] = "*"
            stock1.append(rand1)
            stock1.append(rand2)
            i += 1

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


    if b+2 < 16:
        generateLaby(b+2)







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

generate2()
generateLaby(2)
display()