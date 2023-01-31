#Электронные часы
n = int(input())
h = (n//60)%24
m = n - ((n//60)*60)
print(h,m)
