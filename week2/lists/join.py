pf = ["Pink Floyd", "Metallica", "RHCP","Led Zeppelin","Fleetwood Mac", "Placebo"]
digit = [48,44,18,6,13]
mix = digit + pf
print(mix)

for x in digit:
    pf.append(x)
print(pf)

new =[True, False]
pf.extend(new)
print(pf)


