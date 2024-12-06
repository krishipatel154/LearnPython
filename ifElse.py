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
