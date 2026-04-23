class Car:
    brand = ""
    color = ""
    speed = 0
    def __init__(self,brand,color,speed):
        self.brand = brand
        self.color = color
        self.speed = speed
        
    def Display_Car(self):
        print("Brand: " , self.brand , "|", "Color: " , self.color,"|", "Top Speed: " , self.speed,"km/h", " | Speed Catagory",self.speed_catagory())    
    def speed_catagory(self):
        if self.speed>150:
            return "Fast"
        else:
            return "Normal"

car1 = Car("Toyota", "Red", 200)
car1.Display_Car()
car2 = Car("Honda", "Blue", 220)
car2.Display_Car()

