from functools import reduce

# Functions are block of code which perform specific task
def add(a,b):
    print("sum is:",a+b)

add(10,20)

# lambda function
a = lambda x: print(x)
a(20)

# filter
list1 = [2,4,5,36,65,4,3,6,43]
list2 = list(filter(lambda x: (x%2==0), list1))
print(list2)

# map
list3 = list(map(lambda x:x+1, list1))
print(list3)

# reduce
list4 = reduce(lambda x, y: x+y, list1)
print(list4)