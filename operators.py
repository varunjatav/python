# Operators are used perform operations on variables and values.
# like we use + operator for adding two values eg:- 2+4 --> 6
#print(2+4)
# Python has following operators
# 1) Arithmetic operators (+ , - , /, % , // , **)

#print(10 + 30) # adding two values
#print(40 - 10) # subtract two values
#print(50 / 5) # divide and returns quotient.
#print(50 % 5) # divide and returns remainder.
#print(51 / 5) # divide and returns quotient.
#print(50 // 5) # divide and returns integer quotient by ignoring the decimal value (float).
#print(2**3) # exponents first value by second value


# 2) Assignment Operators ( = , +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=)

a = 4
#print("value assign to variable a =",a)

#+=
# a+= 4  --> a = a + 4 --> a = 4 + 4 --> 8

a += 4
#print("adding a new value to existing value of a using += ",a)

#-= 
# a-=3 -->  a = a - 3 --> 8 - 3 --> 5

a-=3
#print("subtrating 3 from previous value of a", a)


#*=
# a*=10 --> a = a * 10 --> 5 * 10 --> 50

a*=10
#print("Multiply previous value of a by 10", a)

#/=
# a /= 5 --> a = a / 5 --> 50 / 5 --> 10

a/=5
#print("divide previous value of a by 5", a)


#%= 
# a%=5 --> a = a % 5 --> 10 % 5 --> 0
a%=5
#print("remainder value of previous vlue of a after dividing it by 5", a)


x = 50
# //=
# x//=4 --> x = x//4 --> 50 //4 --> 12

x//=4
#print("remaider after removing decimals", x)

# **=
# x **=2 --> x = x**2 --> 12 ** 2 --> 144
x **= 2
#print("x=12 to the power 2", x) 


# &=
# x &=2 --> x = x & 2 --> 10010000   & 0010 -->  0b0 -->
z=5
z&=3
#print(z)


# |=
k = 6

k |= 2

#rint(k)

k^=3
#print(k)

# >>= 3
#print(k)

k <<= 3
#print(k)

#(k:=3)
#print(k:=8)



# comparitive operators

#print( 2 == 2) #True
#print(1 == 2) # False
#print(1 < 2) # True
#print( 1 <= 2) #True
#print( 1>2) # False
#print( 1 >= 2) # False
#print(2>=2) # True
#print(2 !=2 ) # False
#print(1!=2) # True


#Logical Operators (and or not)

#print("and operator")
#print(2 < 5 and 5 < 10)  # True and True --> True
#print(3 < 5 and 12 < 10 ) # True and False --> False
#print(6 < 5 and 4 < 9) # False and True --> False

#print("or operator")
#print(1 < 5 or 5 < 10) # True or True --> True
#print(2 < 3 or 10 < 9) # True or False --> True
#print(6<5 or 9<10) # False or True --> True.
#print(6<5 or 10<9) # False or False --> False

#print("not operator")
#print(not(3 < 2 and 5 < 3)) # 3 < 2 --> False and 5 < 3 --> False --> not(False) --> True
#print(not(False)) # True
#print(not(True)) # False

#Identity Operators 
# These operators are used to compare the objects, not if they are equal, but if they have same memory location.
arr1 = ["apple", "banana", "orange"]
arr2 = ["apple", "banana", "orange"]
arr3 = arr1
print("comparing two arrays")
print(arr1 == arr2) # True
print("using identity operator")
print(arr1 is arr2) # False
print(arr3 is arr1) # True
print(arr3 is not arr1) # False
print(arr2 is not arr1) # True

#membership operators
print("membership operator")
arr1 = ["apple", "banana", "orange"]
print("in membership operator")
print("banana" in arr1)  #True
print("papaya" in arr1)  #False
print("not in membership operator")
print("banana" not in arr1) # False
print("papaya" not in arr1) # True

#Bitwise Operators
#Bitwise operators are used to compare (binary) number
print("bitwise operator")
print("& operator (AND)")
#sets each bit to 1 if both bits are 1
print(6&3)
print("| operator (OR)")
# sets each bit to 1 if one of two bits is 1
print(6|3)

print("^ operator (XOR)")
# sets each bit to 1 if only one of two bits is one.
print(6^3)

print("~ operator (NOT)")
#Inverts all the bits
print(~1)
print("<< operator (Zero fill left shift)")
print(1 << 3)
print(">> operator (Signed right shift)")
print(10 >> 2)