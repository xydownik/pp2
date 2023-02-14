#6
    
class Prime():
    def check(self, n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    def prime(self):
        self.x = lambda a : self.check(a)
        l1 = list(map(int, input().split()))
        l1 = list(filter(self.x, l1))
        print(l1)
x = Prime()
x.prime()   