age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")
else:
    print("You can not vote!")
print("Done")

result = float(input("Enter your result: "))
if result >= 80:
    print("A+")
elif result >= 60 and result <80:
    print("B+")
elif result >= 40 and result <60:
    print("C+")
else:
    print("Fail")
print("Done")

# if-else with data structure
tup1 = ("Web developer","Data Scientist", "php developer")
if 'Web developer' in tup1:
    print("1 is present")
else:
    print("not found")

if tup1[1] == 'Data Scientist':
    print("Done")

list1 = ["Krishi","Savu","Krishna"]
if list1[2] == "Krishna":
    list1[2] = "Mansi"
    print(list1)

dict1 = {
    "Neha":"php",
    "Ramesh":".net",
    "Kanha":"react"
}
if dict1["Kanha"]=="react":
    dict1["Kanha"] = "python"
    print(dict1)

