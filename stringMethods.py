name = "Krishi"
surname = 'Patel'
address = '''
This is a multiline string
which have lot of lines
'''

# String methods
print(len(name))
print(name.upper())
print(name.lower())
print(surname.replace('tel','til'))
print(name.find('i'))
print(address.count('s'))
print('i' in name)
# It doesn't modify the existing string
print(name)
print(surname)
print(address)

# String indexing
print(name[0])
print(name[-1])  #for last character
print(name[-2])
print(name[0:3])  #fetch the part of string
