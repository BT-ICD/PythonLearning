'''
Lab:
Create a student class with a constructor that defines name and marks as instance variables.
An instance method display() will display the values of these variables.
Also create an instance method name calculate() that calculates the grades of the student depending on the ‘marks’.
'''
class Student:
    #constructor
    def __init__(self,n='',m=0):
        self.name=n
        self.marks =m
    #To display student details such as name and marks
    def display(self):
        print('Hi', self.name)
        print('Marks',self.marks)
    #to calculate grade based on marks
    def calculate(self):
        if(self.marks>=600):
            print('First grade')
        elif(self.marks>=500):
            print('Second grade')
        elif(self.marks>=350):
            print('Third grade')
        else:
            print('Fail')

#create instances with some data from keyboard
n = int(input("How many students"))
i=0
while(i<n):
    name = input("Enter Name")
    marks= int(input("Enter Marks"))
    #create an instance of the student class
    s= Student(name,marks)
    s.display()
    s.calculate()
    i+=1
    print("----------------------")