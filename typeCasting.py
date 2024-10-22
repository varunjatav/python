#Typecasting = the process of converting a variable from one datatype to another datatype.
#              str() , int() , float() , bool()

name = "Varun"
name = bool(name)
print(name , type(name))

# type casting of a integer into a float
a = 10
print(a , type(a))
a = float(a)
print(a , type(a))

#type casting of a integer into string
b = 50
print(b , type(b))

b = str(b)
print(b , type(b))

l = int("5")
print(l , type(l))

z = float("5.647")
print(z , type(z))

gpa = 4.9
print(gpa , type(gpa))
gpa = int(gpa)
print(gpa , type(gpa))