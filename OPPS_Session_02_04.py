'''
A Python program to store data into instances using mutator methods and to retrieve data from the instance using accessor methods
'''
class Student:
    #mutator method (setter)
    def setName(self,name):
        self.name = name
    #accessor method (getter)
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks = marks
    def getMarks(self):
        return self.marks

n = int(input("How many students?"))
i=0
while(i<n):
    s=Student()
    name = input("Enter Name")
    s.setName(name)
    marks  = int(input("Enter marks"))
    s.setMarks(marks)
    print('Name',s.getName())
    print('Marks', s.getMarks())
    i+=1
    print('--------------------------')
