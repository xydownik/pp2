#8
a= list(input().split())
def spy_game(l):
    for i in range(len(l)-1):
        if i<=len(l)-3:
            if l[i]=="0" and l[i+1]=="0" and l[i+2]=="7":
                return True
    return False
print(spy_game(a))