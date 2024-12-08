# List is an ordered collection of different type of values enclosed with [].
# Lists are mutable which means we can modify it when we needed.
list1 = [101,"Krishi",92.56]
list2 = [1,2,3,4,5,6]
list3 = [4,7,8,5,6]
print(list1)
print(list2)
print(list3)

# indexing of list
print("access list using index: ")
print(list1[0])
print(list1[-1])
print(list1[0:2])

# list methods
print("List Methods:- ")
print(len(list1))
print(min(list2))
print(max(list2))
# lists are mutable, we can add or delete any element using following methods
print("list append, insert and pop method:- ")
print(list1)
list1.append("Web Developer")  # it add the element at the end of list
print("list1 after append: ",list1)
list1.insert(2,"Artist")
print("list1 after insert: ",list1)
print(list1.pop())   # pop is used to delete last element
print("list1 after pop: ",list1)