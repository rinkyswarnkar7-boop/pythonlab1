#creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "computer science"
}
print("original dictionary:", student)
print("student's name:", student["name"])
print("student's age:", student["age"])
student["grade"] = "A"
print("after adding grade:", student)
student["age"] = 22
print("after updating age:", student)
del student["major"]
print("after deleting major:", student)
print("student details:")
for key, value in student.items():
    print(key,":", value)
print("Does 'grade' exist?", "grade" in student)
print("keys:",student.keys())
print("values:", student.values())
student.keys()

