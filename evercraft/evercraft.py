#alignment copied from Josh's repo; figure out later

class Alignment():
    GOOD, NEUTRAL, EVIL = range(3)

class Character:

    SHEET = {
        "name" : "Yllara",
        "alignment" : Alignment.NEUTRAL,
            #how do I return the human-readable alignment instead of just the index?
        "level": 1,
        "AC" : 5,
        "HP" : 10,
        "abilityScores" : [0, 0, 0, 0, 0, 0]
            #abilityScores indexes: 0=STR, 1=DEX, 2=CON, 3=WIS, 4=INT, 5=CHA
    }
    #how do i manipulate items in a dictionary? REFER TO W3 SCHOOLS




    def __init__(self, name, alignment):
        self.__name = name

    @property 
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

#######################################NAME TESTING#######
#char1 = Character("Sirin")
#print(char1.name)

#char2 = Character("AAA")
#char2.name = "Yllara"
#print(char2.name)


#####################################ALIGNMENT TESTING######
#x = Character.SHEET.get("alignment")
#returns the index of the chosen alignment
#print("This is your alignment")
#print (x)

#Character.SHEET["alignment"] = input("Enter your alignment: ")
#print (Character.SHEET.get("alignment"))

#Character.SHEET.update({"alignment" : (input("What is your alignment? "))})
#print(Character.SHEET.get("alignment"))



