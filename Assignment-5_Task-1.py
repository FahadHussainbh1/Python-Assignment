name = input("Enter your name: ")
num = int(input("Enter a number: "))


if num % 2 == 0:
    print(num,"Even")
else:
    print(num,"Odd")   
print("Numbers from 1 to 5: ")


for i in range(1, num + 1):
    print(i)
print()
print("Countdown: ")

i = num
while i > 0:
    print(i)
    i -= 1

print("Thank you", name) 