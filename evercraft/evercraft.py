class Character:
    def __init__(self, name):
        self.__name = name

    @property 
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

######NAME TESTING#######
#char1 = Character("Sirin")
#print(char1.name)

#char2 = Character("AAA")
#char2.name = "Yllara"
#print(char2.name)


