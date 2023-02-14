#5
from itertools import permutations
def p(s):
    for i in permutations(s):
        print(i)

s=input()
p(s)
