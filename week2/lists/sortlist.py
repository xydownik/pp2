pf = ["Pink Floyd", "Metallica", "RHCP","Led Zeppelin","Fleetwood Mac", "Placebo"]
pf.sort()
print(pf)

digit = [48,44,18,6,13]
digit.sort()
print(digit)

digit.sort(reverse = True)
print(digit)

def myf(x):
    return abs(100-x)
digit.sort(key = myf)
print(digit)

another = [ "Metallica", "RHCP","Led Zeppelin","Fleetwood Mac","bebop","american beauty"]
another.sort()
print(another)

another.sort(key = str.upper)
print(another)

another.reverse()
print(another)

    