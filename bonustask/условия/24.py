# leap year
n = int(input())
if n%4 == 0 or n%400==0:
    if n%100 !=0:
        print("YES")
    else:
        print("NO")