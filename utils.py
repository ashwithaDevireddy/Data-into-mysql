# def mul(a=1,b=3):
#     c=a*b
#     return c

# def add(a=1,b=2):
#     c=a+b
#     return c 

class Student:
    def __init__(self,first,last,kid):
        self.fname = first
        self.lname = last
        self.kid = kid
        self.email =  first + '.' + last +'@tamuk.edu'
    def firstname(self):
        return self.fname


stu_1 = Student('ashwitha','devireddy','k00442409')
stu_2 = Student('santosh','kesireddy','k00442410')

print(stu_1.email)
print(stu_2.email)
print(stu_1.firstname()) 


