#5
class Account():
    def __init__(self,owner,balance=0):
        self.o= owner
        self.b = balance
    def deposit(self, x):
        self.b +=x
    def withdraw(self, y):
        if y<=self.b:
            self.b-=y
        else:
            pass
man = Account("John", 13000)
man.deposit(1000)
print(man.b) 
man.withdraw(150)
print(man.b)