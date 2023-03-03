def myfunc():
  x = 300
  print(x)       #local var

myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)            #inner function
  myinnerfunc()

myfunc()

x = "var"
def Print():
    print(x)            #global variable x
Print()
print(x)
print("\n")

def printlocal():
    x = "war"
    print(x)
printlocal()         #local and global
print(x)

def globword():
    global x
    x = "asd"       #make the var global
globword()    
print(x)


