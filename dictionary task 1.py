students = {
    "name": ["Ali", "Sara", "Ahemd"],
    "marks": [80, 90, 75] 
}

print(students.get("name"))
print(students.get("marks"))
print(max(students.get("marks")))

highest_marks = max(students.get("marks"))


for name, marks in zip(students.get("name"), students.get("marks")):
    if marks == highest_marks:
        print(name, highest_marks)