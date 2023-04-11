class school():
    def __init__(self,schoolname):
        self.schoolname = schoolname
        
    def func1(self):
        print("School")
class student1(school):
    def __init__(self, name1,schoolname):
        self.name1= name1
        super().__init__(schoolname)
    def func2(self):
        print("st1")
class student2(school):
    def __init__(self, name2,schoolname):
        self.name2 = name2
        super().__init__(schoolname)
class student3(student1,student2,school):
    def __init__(self,name1,name2,name3,schoolname):
        self.name3 = name3
        super().__init__(name1, schoolname )
        super().__init__(name2,schoolname )
        super().__init__(schoolname)
    def func3(self):
        print(self.name1,self.name2,self.name3,self.schoolname)
        
x = student3("st1","st2","st3","school")
x.func3()