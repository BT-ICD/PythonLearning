'''
Constructor with parameter - paremeterized constructor
'''
class Student:
    def __init__(self, rollno=0, name='',semester=None):
        self.rollno = rollno
        self.name=name
        self.semester=semester
    def printData(self):
        print("Roll Number",self.rollno, " Name ", self.name, "Semester",self.semester)

s1 = Student()
s1.printData()


s2 =Student(101,'Minaxi',4)
s2.printData()