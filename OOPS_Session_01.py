"""
Creating class - Session 01
Class Student
Student is a name of a class. Generally class name starts with capital letter
It has 3 attributes such as name, rollno, semester
It has 1 method to print data members
__init__ is a special method to initialize the variable (data member)
self is a variable that refers to current instance.
Variable rollno, name, semester are called instance variables. To refer to instance variables, we can use . operator notation along with self as: self.semester
Method printData is called the instance method. Instance method use 'self' as the first parameter that refers to the
"""
class Student:
    def __init__(self):
        self.rollno =1
        self.name="Rajesh"
        self.semester = 1
    def printData(self):
        print("Roll number:", self.rollno," Name: ", self.name, "Semester: ",self.semester)
# To create an instance of a Student class
s1 = Student()
# call (invoke) method printData on the Student instance s1
s1.printData()

