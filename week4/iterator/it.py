t1 = ("Pink Floyd", "Metallica", "B.B.King")
it = iter(t1)
print(next(it))        #iterator for tuple
print(next(it))
print(next(it))

s1 = "KBTU"
it2 = iter(s1)      #for strings
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for x in t1:
    print(x)            #output through "for"
    
for x in s1:
    print(x)
    
class MyNums:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

c1 = MyNums()
myit = iter(c1)

print(next(myit))
print(next(myit))       #iterator for class
print(next(myit))
print(next(myit))
print(next(myit))
    
class Nums:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a<=20:
        x = self.a
        self.a += 1
        return x
    else:
        raise StopIteration     #StopIteration
print("\n")    

a = Nums()
it3 = iter(a)
for x in a:
    print(x)

