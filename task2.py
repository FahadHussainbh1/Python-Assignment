passed=0
fail=0
highest=0
for i in range (1,6):
 marks = input("Enter your marks:" )
 marks = int(marks)
 if marks > highest:
    highest = marks 
 if marks >= 80:
    print("Grade: A")
    passed+=1         
 elif marks >= 60:
    print("Grade: B")
    passed+=1
 elif marks >= 50:
    print("Grade: C")
    passed+=1
 else:
    print("Fail")
    fail+=1  

print("Number of students who passed:", passed)
print("Number of students who failed:", fail)
print("Highest marks:", highest)