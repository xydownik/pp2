#creating and calling a function
def user():
    fname = input()
    lname= input()
    print("Welcome back,",fname,lname+"!")
user()

#arguments and number of arg
def trumps(name = "George",sname = "Washington" ):
    print(name, sname)
fname = "Donald"
lname = "Trump"
trumps(fname,lname)

#arbitrary arg
def dead(*group):
    print("Dead one is "+ group[2])
dead("Robert Plant", "David Gilmour", "Syd Barrett")

#keyword arg
def alive(m1,m2,m3):
    print("Alive one is "+ m2)
alive(m1 = "Janis Joplin", m2 = "Jimmy Page", m3 = "John Lennon")

#arbitary keyword arguments
def fullname(**user):
    print("My last name is "+ user["sname"])
fullname(name = "Aruzhan", sname = "Sazanova")

#default parameter
trumps()

print("\n")
#List as an arg
def cout(list1):
    for  i in list1:
        print(i)
l1 = ["Robert Plant", "David Gilmour", "Syd Barrett"]
cout(l1)

#return values
def sqr(x):
    return x**2
print(sqr(3))

#pass
def my_func():
    pass

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(5)



