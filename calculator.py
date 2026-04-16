def add(num1, num2):
    print(num1, "+", num2, "=", num1 + num2)
def subt(num1, num2):
    print(num1, "-", num2, "=", num1 - num2)
def mult(num1, num2):
    print(num1, "*", num2, "=", num1 * num2)
def div(num1, num2):
    print(num1, "/", num2, "=", num1 / num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(1,"Addition") 
print(2,"Subtraction") 
print(3,"Multiplication") 
print(4,"Division")
print(5,"Exit")
choice = int(input("Your Choice : "))

while(True):
    if choice == 1:
        add(num1, num2)
        break
    elif choice == 2:
        subt(num1, num2)
        break
    elif choice == 3:
        mult(num1, num2)
        break
    elif choice == 4:
        div(num1, num2)
        break
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid Choice")
        break