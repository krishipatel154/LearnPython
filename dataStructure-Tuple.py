# Tuple is an ordered collection of different type of elements enclosed with ().
# Tuples are immutable
# Duplicates are allowed in tuple
tup1 = (101,"Sneha",89.45)
tup2 = (1,2,3,4,5)
tup3 = (4,5,6,7,4)

# indexing of tuple
print("indexing of tuple")
print(tup1[0])
print(tup1[-1])  # used to print last element
print(tup1[0:2])  # print the element from 0 to 1 position

# tuple methods
print("Length of tup2: ",len(tup2))
print("Minimum of tup2: ",min(tup2))
print("Maximum of tup2: ",max(tup2))
# min and max method for strings
print("min and max for strings")
strTup = ("a","b","A","c","B")
print(min(strTup))
print(max(strTup))

# concatenating tuples
print("concatenating tuples")
print(tup2+tup3)
print(tup3+tup2)
print((tup1*3)+tup2)


