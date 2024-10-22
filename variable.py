# variables are the container that holds the data 
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


def myFunc(): 
    global a ,b
    a , b = 10 , 15
    print(a+b)

myFunc()

print(a+b)

print(x ,type(x))
print(y , type(y))
print(z , type(z))
print(p , type(p))
print(complex , type(complex))
print(list , type(list))
print(tup , type(tup))
print(range , type(range))
print(dict , type(dict))
print(set, type(set))
print(frozen , type(frozen))
print(byt, type(byt))
print(bytearr , type(bytearr))
print(mem, type(mem))
print(none, type(none))