import random
import datetime
import pygame
class Character:

    def __init__(self,name,haut,droite,gauche,bas):
        self.touche = [haut,bas,droite,gauche]
        self.haut = haut
        self.droite = droite
        self.gauche = gauche
        self.bas = bas
        self.name = name
        self.x = 0
        self.y = 0
        if name == "Mirabelle":
            self.skin = "V"
        elif name == "Jose":
            self.skin = "H"
        elif name == "Bob":
            self.skin = "P"
        self.score = 0
        self.pourcentage = 100
        self.isParalize = False
        self.second = 0
        self.maxSecond = 0


    def addPercent(self,percent):
        if self.pourcentage+percent >= 100:
            self.pourcentage = 100
            ultiSound = pygame.mixer.music.load('ulti.wav')
            pygame.mixer.music.play()
        else:
         self.pourcentage = self.pourcentage+percent


    def use_ultime(self,laby,ennemie):
        print("tentative d'ultime en cours...")
        if self.pourcentage == 100:

            if self.name == "Mirabelle":
                self.M_ult(laby,ennemie)
            elif self.name == "Jose":
                self.J_ult(laby)
            elif self.name == "Bob":
                self.B_ult(ennemie)

        else:
            print("Votre ultime n'est pas charger")


    def M_ult(self,laby,ennemie):
        i = "X"
        rand1 = 0
        rand2 = 0
        while i != "*":
            rand1 = random.randint(0, 9)
            rand2 = random.randint(0, 9)
            i = laby[rand1][rand2]
        laby[rand1][rand2] = ennemie.skin

        laby[ennemie.x][ennemie.y] = "*"

        ennemie.x = rand1
        ennemie.y = rand2
        self.pourcentage = 100
        return [rand1,rand2,ennemie.x,ennemie.y]

    def J_ult(self,laby):
        y = self.y
        for i in [0,1,2,3,4,5,6,7,8,9]:
            if laby[i][y-1] == "P" or laby[i][y-1] == "H" or laby[i][y-1] == "V" or laby[i][y-1] == "=" or laby[i][y-1] == "+":
                print()
            else:
                laby[i][y-1] = "X"
                return [i,y-1]
        self.pourcentage = 0

    def B_ult(self,ennemie):
        g = ennemie.gauche
        d = ennemie.droite
        h = ennemie.haut
        b = ennemie.bas

        ennemie.gauche = d
        ennemie.droite = g
        ennemie.haut = b
        ennemie.bas = h

        self.pourcentage = 0


    def getsecond(self):
        test = datetime.now()
        test = str(test)
        test = test.split(" ")
        test = test[1]
        test = test.split(":")
        test = test[2]
        test = test.split(".")
        test = test[0]
        test = int(test)
        return test

    def move_bottom(self,laby):


        if laby[self.x][self.y + 1] == "*":
            laby[self.x][self.y + 1] = self.skin
            laby[self.x][self.y] = "*"

            self.x = self.x
            self.y = self.y + 1
        elif laby[self.x][self.y + 1] == "+":
            self.score += 1
            return True
        elif laby[self.x][self.y + 1] == "=":
            laby[self.x][self.y + 1] = self.skin
            laby[self.x][self.y] = "*"

            self.x = self.x
            self.y = self.y + 1
            self.addPercent(20)
        return [self.x, self.y]

    def move_right(self,laby):

        if laby[self.x + 1][self.y] == "*":
            laby[self.x + 1][self.y] = self.skin
            laby[self.x][self.y] = "*"
            self.x = self.x + 1
            self.y = self.y
        elif laby[self.x + 1][self.y] == "+":
            self.score += 1
            return True
        elif laby[self.x + 1][self.y] == "=":
            laby[self.x + 1][self.y] = self.skin
            laby[self.x][self.y] = "*"
            self.x = self.x + 1
            self.y = self.y
            self.addPercent(20)
        return [self.x, self.y]
    def move_left(self,laby):


        if laby[self.x - 1][self.y] == "*":
            laby[self.x-1][self.y ] = self.skin
            laby[self.x][self.y] = "*"
            self.x = self.x - 1
            self.y = self.y
        elif laby[self.x - 1][self.y] == "+":
            self.score += 1
            return True
        elif laby[self.x - 1][self.y] == "=":
            laby[self.x-1][self.y] = self.skin
            laby[self.x][self.y] = "*"
            self.addPercent(20)
        return [self.x, self.y]

    def move_top(self,laby):

        if laby[self.x][self.y - 1] == "*":
            laby[self.x][self.y - 1] = self.skin
            laby[self.x][self.y] = "*"
            self.x = self.x
            self.y = self.y - 1
        elif laby[self.x][self.y - 1] == "+":
            self.score += 1
            return True
        elif laby[self.x][self.y - 1] == "=":
            laby[self.x][self.y - 1] = self.skin
            laby[self.x][self.y] = "*"
            self.addPercent(20)

        return [self.x, self.y]


    def backup_touche(self):
        self.haut = self.touche[0]
        self.bas = self.touche[1]
        self.droite = self.touche[2]
        self.gauche = self.touche[3]

