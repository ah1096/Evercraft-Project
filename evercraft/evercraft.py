class Character:

    ABILITIES = {
        "STR" : 10,
        "CON" : 10,
        "DEX" : 10,
        "WIS" : 10,
        "INT" : 10,
        "CHA" : 10
    }


#remove user inputs later?
    def __init__(self, name = "Hugh Mann", alignment = "neutral"):
        name = str(input("What is your name? "))
        self.name = name

        alignment = str.lower(input("Enter your alignment: Good, Neutral ,or Evil. "))
        self.alignment = alignment

        print (f"Your name is {self.name} and your alignment is {self.alignment}")


char1 = Character("Yllara")
#print (f"Your name is {char1.name}, and your alignment is {char1.alignment}")

#char2 = Character("Sirin", "good")
#print (f"Your name is {char2.name}, and you are a {char2.alignment} character")





