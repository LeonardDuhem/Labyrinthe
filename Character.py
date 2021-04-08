import random


class Character:

    def __init__(self,name):
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
        self.bonus = False
        self.nomBonus = ''
        self.pourcentage = 0
        self.ultime = False


    def use_ultime(self,laby,ennemie):
        if self.name == "Mirabelle":

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


    def move_bottom(self,laby):
        print("on m'a appelé?")
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
            self.pourcentage += 20


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
            self.pourcentage += 20

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
            self.pourcentage += 20

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
            self.pourcentage += 20



