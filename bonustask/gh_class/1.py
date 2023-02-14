#1
class Word():
    def getString(self):
        self.word = input()
    def printString(self):
        print(self.word.upper())
obj = Word()
obj.getString()
obj.printString()