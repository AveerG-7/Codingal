class School:
    def __init__(self,section,classname):
        self.classname = classname
        self.section = section
    
class Student(School):
    def __init__(self,section,name,roll_no,classname):
        self.name= name
        self.roll_no = roll_no
        School.__init__(self,section,classname)
    
s = Student('F',"Aveer",7,7)
result = ("Section is",s.section, "Name is" ,s.name,"Roll number is", s.roll_no, "Grade is ",s.classname)
print(result)


        