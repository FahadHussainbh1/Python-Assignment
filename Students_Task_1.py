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
Student1.Display_result()

Student2 = Student("Ali", 80)
Student2.Display_result()

Student3 = Student("Ahem",70)
Student3.Display_result()

Student4 = Student("Mudasir",60)
Student4.Display_result()
