#Tuples are one of the built in datat types in python.
#used to store ultiple datat in sngle variable.
#tuples is a collection of data which are in order and unchangeable, and also allow duplicate values.
# tuples are built by using parenthesis or round brackets ()

myTuple = ("a","a", "b", "c", "d", "e")
numberTuple = (1,2,3,4,5,6,4,5)
print(myTuple)
print(type(myTuple))

print(numberTuple)
# tuple Items 
# we can use indexes to access tuple items.
print(myTuple[0])  # first item of tuple
print(myTuple[1])  # second item of tuple
#last item of tuple
print(myTuple[-1]) # last item of tuple
print(myTuple[len(myTuple) - 1])

#length of tuple
print(len(myTuple))

#create a tuple with one item
x = (1)  #wrong --> it is not a tuple.
print(x)
y = (1,) # right --> this is a tuple
print(y)


#tuple item data types
string = ("rahul", "kavita", "simran", "akshay") # tuple that store string data type.
print(string)
print(type(string)) # class tuple
print(type(string[0])) # class str

numbers = (1,2,3,4,5,6) # tuple that has tuple items as int data type.
print(numbers)
print(type(numbers)) # class tuple
print(type(numbers[0])) # class int

# mixed datatypes
mixed = ("kavita", True, 45, 30.6) # tuple that has tuple item of mixed data types
print(mixed)
print(type(mixed)) # class tuple
print(type(mixed[0])) # class str
print(type(mixed[1])) # class bool
print(type(mixed[2])) # class int
print(type(mixed[3])) # class float


# the tuple() constructor 
const = tuple(('a', 'b', 'c'))
print(const)

#update tuples
#convert a tuple into a list
a = list(const)
#change the list first item 
a[0] = "x"
#covert list back to tuple
const = tuple(a)
print(const)

#unpacking a tuple
(a,y,z) = const
print(a,y,z)
# to access remaining values use *
(a,*x) = const
print(x) #['b','c']
colors = ('red', 'green', 'blue', 'black', 'yellow', 'white')
(a,*b,c) = colors
print(a) # red
print(c) # white
print(b) #[green,blue,black,yellow]


#loop through tuple items using for loop iteration
#for i in colors:
 #   print(i)

#loop through indexes using for loop iteration
#for i in range(len(colors)):
 #@   print(i)

#using a while loop

#initialze iterator on 0
i=0
while i < len(colors):
    #print(i)
    #it will loop the indexes of each item
    print(colors[i],i)
    #it will print each item of tuples
    i+=1
    


#Join Tuples
print("Join Tuples using + operator")
tuple1 = ('a','b','c')
tuple2 = (1,2,3,3,3)
print(tuple1+tuple2)

#Multiply Tuples
print("multiply a tuple by 2")
tuple1 = tuple1*2
print(tuple1)  # ('a','b','c','a','b','c')

tuple2 = tuple2*2
print(tuple2) # (1,2,3,3,3,1,2,3,3,3)

#count --> count the number of times the input is occured in tuple 
print(tuple2.count(3) )# 6
print(tuple1.count('a')) #2
print(tuple2.count(1)) #2

#index --> search first occurance of input item in the tuple
print(tuple2.index(1)) #  1 --> on index 0 --> 0
print(tuple2.index(3)) # 3 --> on index 2 --> 2