num = [1,2,3,4,5,6]
print(num)

print("Maximum Number:")
print(max(num))

print("Minimum Number:")
print(min(num))

print("Sum of all numbers:")
print(sum(num))  

print("Even numbers:")
for x in num:
    if x % 2 == 0:
        print(x, "Even")