class Animal:
    name = ""
    sound = ""
    legs = 4

    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(self.name , " says " , self.sound , "It has " , self.legs , " legs")


Wolf = Animal("Wolf", "Howl")
Lion = Animal("Lion", "Roar")
Horse = Animal("Horse", "Neigh")   
Lion.speak()
Wolf.speak()
Horse.speak()