#List
fruitList = ['apple', 'banana', 'orange', 'pineapple', 'guava']


#List Items
#ordered , changeable, and allow duplicate values
#list items are indexed. starting from 0.

#list length
#length defines the number of items present inside the list.
#we have to use len() method to get the length of the list
#syntax
#len(fruitList)
#print(len(fruitList))

#List Data Types
#list can be of any data type
#string, int, boolean, float
stringList = ['rahul', 'aryan' , 'arjun' , 'kirti']
#print("list containing strings",stringList)

numberList = [10, 20, 30 , 40]
#print("list containing numbers",numberList)

boolList = [True, False, True]
#print("list containing boolean",boolList)

floatList = [12.4 , 13.6 , 20.5 , 45.9]
#print("list containing floats",floatList)

#single list can contain different data types also.
mixedList = [1,2,'arjun', 'kirti', False,True,12.5]
#print("list containing different data types", mixedList)

#list type.
#print(type(stringList))
#print(type(numberList))
#print(type(boolList))
#print(type(floatList))
#print(type(mixedList))

#list constructor
print("list constructor")
newList = list(("apple", "banana", "guava"))
print(newList)

nameList= ['arjun', 'kirti', 'shubham', 'adhvay']
print(nameList)
print("first name", nameList[0])
print("second name", nameList[1])
print("last name", nameList[len(nameList) -1])
print("last name ", nameList[-2])

# Range List
#by giving starting index and endeing index as well
print(nameList[1:3])

#by giving only starting index
print(nameList[2:])

#by giving only ending index
print(nameList[:2])

#begative indexing if want to start from last of the list
print(nameList[-3:-1])

#check if item includes

if "varun" in nameList:
    print("Yes present")
else:
    print("Not present")

#Change Item value.
#change single item in list
nameList[0] = 'varun'
print(nameList)

#change range of item values.
print(len(nameList))
nameList[1:2] = ["kartik", "ayush"]
print(nameList)
print(len(nameList))

nameList[1:3] = ["ajay"]
print(nameList)
print(len(nameList))

#add list items
#insert method
nameList.insert(2,"poonam")
print(nameList)
print(len(nameList))

#append method

nameList.append("kavita")
print(nameList)

#extend lists

fruits = ["mango", "pineapple" , "papaya"]
vegies = ["potato", "onion", "brinjal","onion"]
fruits.extend(vegies)
print(fruits)

#append any iterable object like tuples, sets, dictionary

thistuple = ('kiwi', 'orange')
fruits.extend(thistuple)
print(fruits)

#remove list item from list
fruits.remove("onion")
print(fruits)

#remove specified index
#pop(index) --> removes item which matches the index
fruits.pop(0)
print(fruits)

#pop() --> remooves last item
fruits.pop()

#del keyword alos removes specified index and also delete thelist completely
del fruits[1]
print(fruits)

del fruits
#print(fruits)

#clear the list items 
myList = ["Goa", "Manali", "Kashmir", "Pune"]
print(myList)
myList.clear()
print(myList)


# Loops Through a list
myList2 = ["Goa", "Manali", "Kashmir", "Pune"]
#using for loop / in
for x in myList2:
    print(x)

#loop throught index number
# use range and len functions

for i in range(len(myList2)):
    print(myList2[i], i)


#using while loop

i = 0
while i < len(myList2):
    print(myList2[i], "usimg while loop")
    i+=1

# using short hand for loop
#[print(x) for x in myList2]
#newList = [x for x in myList2 if "a" in x ]

#simple for loop
#for x in myList2:
 #   if "a" in x:
  #      print(x)

fruits = ["apple", "orange", "banana"]
newList = ["apple" for x in fruits]
print(newList)


#Sort the list
name = ["Ajay", "Bahan", "David", "Gaurav","Emily", "Chris"]

print("sorting name lists alphabetically ascending")
name.sort()
print(name)
print("sorting name list alphabetically descending")
name.sort(reverse=True)
print(name)

number = [3,1,4,2,6,5]
print("sorting number lists in ascending order")
number.sort()
print(number)
print("sorting number list in descending order")
number.sort(reverse = True)
print(number)

# customize sort function

#def Sorting(n):
   #return abs(n - 50)
#thisList = [100,42,54,50,12,23,89]
#thisList.sort(key = Sorting)
#print(thisList)

#sort is case insensitive
fruits = ["apple", "Orange", "banana", "Pineapple"]
fruits.sort()
print(fruits)

fruits.sort(key = str.lower)


print(fruits)
#reverse method

cities = ["Jhansi", "Gwalior", "Dehli", "Mumbai", "Pune"]
cities.reverse()
print(cities)

roll_no = [3,15,4,16,2,12]
roll_no.reverse()
print(roll_no)


#Copy Lists
#by using copy method
print("copying lists using cop method...")
yourList = ["Akash", 21, "Mumbai", True]
myList = yourList.copy()
yourList.append("dasd")
print("Your List",yourList)
print("My List",myList)

# by using list() method.
thirdList = list(myList)
print("third list",thirdList)

# by using slice operator
fourthList = yourList[:]
print("fourth List",fourthList)

#Join two lists
# + operator
list1 = ["a", "b", "c"]
list2 = [1,2,3]
#print(list1+list2)


#join list 2 to list 1 one by one

#for i in list2:
#  list1.append(i)

#print(list1)

#by using extend method
#list1.extend(list2)
#print(list1)