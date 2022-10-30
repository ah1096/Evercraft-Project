
class Character:

    SHEET = {
        "name" : "Yllara",
        "alignment" : {
            "neutral" : true,
            "good" : false,
            "evil" : false,
        },
            #how do I return the human-readable alignment instead of just the index? XXXX
            #changed to a nested dictionary to experiment with changing alignment???
        "level": 1,
        "AC" : 5,
        "HP" : 10,
        "abilityScores" : {
            "STR": 10, 
            "DEX": 10, 
            "CON": 10, 
            "WIS": 10, 
            "INT": 10, 
            "CHA": 10}
            #changed abilityscores into a nested dictionary for easier readability
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



