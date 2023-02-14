s = input()
def palin(s):
    s2 = s[::-1]
    cnt=0
    for i in range(0,len(s)):
        if s[i] == s2[i]:
            cnt+=1
    if cnt == len(s):
        return True
    return False
print(palin(s))