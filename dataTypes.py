# variables can hold different data types different data types can do different things

# different datatypes
x = 9 #holding number
y = "python" # holding string
z = True #holding boolean value
p = 10.9 #holding float value
complex = 1j # holding complex data type
list = [1, 2, 3, 4, 5, 6, 7, 8] # holding list of numbers
tup = ("apple", "banana" , "mango") # holding tupple
range = range(6) # holding range from 0 -> 6
dict = {"name": "John", "age": 36} # holding dictionary
set = {"apple", "orange", "banana"} # holding set
frozen = frozenset({"apple", "orange", "banana"}) # holding frozenset
byt = b"Hello" # holding bytes
bytearr = bytearray(5) # holding bytearray
mem = memoryview(bytes(5)) # holding memoryview of bytes 
none = None # holding none datatype

#Strings

first_name = "John"
fav_food = "Pizza"
email = "John@example.com"
#print(F"Hello {first_name}")
#print(f"Your favourite food is {fav_food}")
#print(f"Your email is {email}")

#Integers 

age = 25
quantity = 3
number_of_students = 100
#print(f"You are {age} years old")
#print(F"You bought {quantity} shirts")
#rint(f"Total Number of students are {number_of_students}")


#Floats
price = 10.99
gpa=7.0
distance = 2.5
print(f"The price is {price}")
print(f"My gpa is {gpa}")
print(f"The distance is {distance} km")

#boolean

is_student = True
print(f"Are you a student?")
if(is_student):
    print("Yes, I am a student")
else: 
    print("No, I am not a student")

for_sale = True

if(for_sale):
    print("This Item is for sale")
else: 
    print("This Item is not for sale")

is_online = False

if(is_online):
    print("I am online")
else:
    print("I am not online")