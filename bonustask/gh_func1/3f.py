#3
def solve(numheads,numlegs):
    r = numlegs//2 - numheads
    c = numheads - r
    return r,c
print(solve(35,94))