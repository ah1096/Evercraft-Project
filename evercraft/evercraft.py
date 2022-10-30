class Character:

    AB_SCORES = {
        "STR" : 10,
        "CON" : 10,
        "DEX" : 10,
        "WIS" : 10,
        "INT" : 10,
        "CHA" : 10
    }


#remove user inputs later?
    def __init__(self, name = "Hugh Mann", alignment = "neutral"):
        #name = str(input("What is your name? "))
        self.name = name

        #alignment = str.lower(input("Enter your alignment: Good, Neutral ,or Evil. "))
        self.alignment = str.lower(alignment)
        #.lower makes alignment input look nicer when printed

        print (f"Your name is {self.name} and your alignment is {self.alignment}")

        self.hp = 10
        self.ac = 5

        self.dmg = 1



        roll = int(input("Enter a number between 1 and 20: ")

        def attack(self, ATKroll, foe):
            if (ATKroll<20 and ATKroll >= foe.ac):
                foe.hp == foe.hp - self.dmg
            elif (ATKroll == 20):
                foe.hp == foe.hp - (self.dmg * 2)
            else:
                print(f"Oops, your didn't hit {foe.name}")




char1 = Character("Yllara", "good")
print (char1.hp)

foe = Character("Arally", "EvIl")
print (foe.hp)







