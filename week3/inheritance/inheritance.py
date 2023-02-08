class person():
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
    def fullname(self):
        print(self.fname, self.lname)
        
x  = person("Ponimayu", "Ponimayev")
x.fullname()       

class student(person):
    pass

x = student("Ponimayu", "Ponimayev")
x.fullname()

class student(person):
    def __init__(self, fname, lname):
        person.__init__(self,fname, lname)
x = student("Ponimayu", "Ponimayev")
x.fullname()

class son(person):
    def __init__(self, fname, lname,year ):
        super().__init__(fname, lname)
        self.graduation = year
    
    def welcome(self):
        print("Welcome,", self.fname, self.lname,",to the greatest party of alumni", self.graduation)
x = son("Ponimayu", "Ponimayev", 2018)
x.fullname()
x.welcome()
