'''
References:
Comments are hints that we add to our code to make it easier to understand.
Comments: https://www.programiz.com/python-programming/comments
Variable: In programming, a variable is a container (storage area) to hold data.
https://www.programiz.com/python-programming/variables-constants-literals
Datatypes: Numeric, String, Boolean
We can use the type() function to know which class a variable or a value belongs to.
https://www.programiz.com/python-programming/variables-datatypes
Type Conversion:
In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.
https://www.programiz.com/python-programming/type-conversion-and-casting
'''

a = input("Enter value 1")
b = input("Enter value 2")
print(a+b)
print(type(a))

#Conversion from string to int
a= int(input("Enter value 1"))
b = int(input("Enter value 2"))
print(a+b)
print(type(a))
#Conversion from string to float
c= float(input("Enter value 1"))
d= float(input("Enter value 2"))
print(c+d)
print(type (c))

#Assignment Operators
a=10
print(a)
a+=5
print("Value of a after a+5",a)
