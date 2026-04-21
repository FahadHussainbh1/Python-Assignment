class Student:
    name = ""
    marks = 0

    print("Your Results")

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def Display_result(self):
        if self.marks >= 85:
            print(self.name + ":" " got A1 grade")
        elif self.marks >= 75:
            print(self.name + ":" " got A grade")
        elif self.marks >= 65:
            print(self.name + ":" " got B grade")
        elif self.marks >= 50:
            print(self.name + ":" " got C grade")
        else:
            print(self.name + " You are fail")            


Student1 = Student("Fahad", 90)
Student2 = Student("Ali", 80)
Student3 = Student("Ahmed", 67)
Student4 = Student("Sara", 57)
Student5 = Student("Hussain", 45)

Student1.Display_result()
Student2.Display_result()
Student3.Display_result()    
Student4.Display_result()
Student5.Display_result()
