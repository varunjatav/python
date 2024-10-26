#Sets are used to store multiple values in single variable
#Sets are unordered, unchangeable and unindexed
#Sets are written in curly brackets {}
myset = {'apple', 'banana', 'orange'}
print(myset)

#Set Item
# set items are unordered, unchangeable and do not allow duplicate values.
# duplicate items
# True and 1 will be considered as one value. similarly False and 0
duplicateset = {'apple', 'banana', 'orange', 'orange', 1, True, False, 0}
print(duplicateset)

# get length
print(len(duplicateset))

#set items
# string
string = {"varun", "ajay", "vicky", "kavya"}
print(string, type(string))

#number 
numbers = {1,2,3,4,5,6}
print(numbers, type(numbers))

#float
floats = {0.2,3.4,1.6,7.8}
print(floats, type(floats))

#boolean
boolean = {True, False}
print(boolean, type(boolean))

# we can create set using construtor
thisset = set(("a",'b', 'c'))
print(thisset, type(thisset))

# access set items
# using loop
for i in thisset:
    print(i)

# by checking if item present in set
print('a' in thisset)
#ckeck if ont present
print('a' not in thisset)


#Add items
# to add one item use add() method
thisset.add("d")
print(thisset)

#Add Sets
# to add items from another set to current set use update() method.

newset= {'x','y', 'z'}
thisset.update(newset)
print(thisset)

# we can add any iterables like set lists into set using update
thislist = ['k','l','m']
thisset.update(thislist)
print(thisset)

#Remove set items
