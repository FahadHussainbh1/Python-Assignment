class Animal:
    name = "Dog"
    sound = "Woof"

    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(self.name + " says " + self.sound)


Dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")
cat.speak()    
Dog.speak()    
