# set is an unordered and unindexed collection of elements enclosed with {}
# sets are mutable
# duplicates are not allowed in set
set1 = {101,"abc",67.44,True}
set2 = {1,2,3,4,4,5}
set3 = {6,7,8,4,8,0}
print(set1)
print(set2)

# set methods
set1.add(20)   # it is used to add single value at a time
set2.update([4,6,7,8])  # it is used to add multiple values
set1.remove("abc")
set2.union(set3)
set2.intersection(set3)
print(set1)
print(set2)
print(set3)


