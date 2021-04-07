
def ChooseClass():

    print('\33[1m' +"Bienvenue, joueur 1"+ '\33[0m')
    print('\33[35m' +"Tu as le choix entre 3 classes"+ '\33[0m')
    print("1: Bob. Pouvoir: ...")
    print("2: José. Pouvoir: ...")
    print("3: Mirabelle. Pouvoir: ...")

    input1 = input()

    if(input1 == "1"):
        print("vous avez choisi la classe Bob")
        joueur1 = 'Bob'
    elif (input1 == "2"):
        print("vous avez choisi la classe José")
        joueur1 = 'José'
    elif (input1 == "3"):
        print("vous avez choisi la classe Mirabelle")
        joueur1 = 'Mirabelle'