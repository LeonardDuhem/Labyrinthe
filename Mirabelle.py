import random


class Mirabelle:

    def __init__(self):
        self.name = "Mirabelle"
        self.x = 0
        self.y = 0
        self.skin = "V"
        self.score = 0
        self.bonus = False
        self.nomBonus = ''
        self.pourcentage = 0
        self.ultime = False  #TP ennemie

    def use_ultime(self,laby,ennemie):
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

    def test(self):
        print("coucou")