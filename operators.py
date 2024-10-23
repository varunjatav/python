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
print("value assign to variable a =",a)

#+=
# a+= 4  --> a = a + 4 --> a = 4 + 4 --> 8

a += 4
print("adding a new value to existing value of a using += ",a)

#-= 
# a-=3 -->  a = a - 3 --> 8 - 3 --> 5

a-=3
print("subtrating 3 from previous value of a", a)


#*=
# a*=10 --> a = a * 10 --> 5 * 10 --> 50

a*=10
print("Multiply previous value of a by 10", a)

#/=
# a /= 5 --> a = a / 5 --> 50 / 5 --> 10

a/=5
print("divide previous value of a by 5", a)


#%= 
# a%=5 --> a = a % 5 --> 10 % 5 --> 0
a%=5
print("remainder value of previous vlue of a after dividing it by 5", a)


x = 50
# //=
# x//=4 --> x = x//4 --> 50 //4 --> 12

x//=4
print("remaider after removing decimals", x)

# **=
# x **=2 --> x = x**2 --> 12 ** 2 --> 144
x **= 2
print("x=12 to the power 2", x) 


# &=
# x &=2 --> x = x & 2 --> 10010000   & 0010 -->  0b0 -->
z=5
z&=3
print(z)


# |=
k = 6

k |= 2

print(k)
