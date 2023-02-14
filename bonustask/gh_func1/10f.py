l1 = list(map(int, input().split()))
def unique(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2
print(unique(l1))