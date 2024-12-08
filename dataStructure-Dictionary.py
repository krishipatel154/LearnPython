# Dictionary is an unordered collection of key:value pair enclosed with {}.
# It is mutable
students = {
    "Krishi":89.45,
    "Savu":78,
    "Krishna":67
}
teachers = {
    "Arti":"Web",
    "Neha":"app"
}
print(students)

print(students["Krishi"])
print(students.keys())
print(students.values())
print(students.items())

# How to add or delete any pair from dictionary
print(students)
students["Savu"] = 79
print("dictionary after modify: ",students)
students["Mansi"] = 44
print("dictionary after append: ",students)
students.update(teachers)
print("dictoinary after update: ",students)
print(students.pop("Savu"))
print(students)
