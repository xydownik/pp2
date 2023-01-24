t = 'pink floyd'
print(1, t.capitalize())
t = "Pink Floyd"
print(2,t.casefold())
print(3,t.center(20))
print(4,t.count("Pink"))
print(5,t.encode())
print(6,t.endswith('d'))
a= "P\tI\tN\tK"
print(7,a.expandtabs(10))
print(8,t.find("Floyd"))
b=6
c="SIGMA {}"
print(9,c.format(b))
d = {'num' : '10'}
print(10, "SIGMA {num}".format_map(d))
print(t.index('l'))
print(11,"SIGMA6".isalnum())
print(12, "SIGMA".isalpha())
print(13, "\u0033".isdecimal())
print(14, "1969".isdigit())
print(15,"PINK".isidentifier())
print(16,'&',21,"pinkfloyd".islower(), "SIGMA".isupper())
print(17,"1234".isnumeric())
print(18,"\tsig\tma".isprintable())
print(19," ".isspace(),"\t".isspace())
print(20, t.istitle(), "pink FLOyd".istitle())
f=("Metallica","Pink Floyd", "B.B.King" )
print(" & ".join(f))
print("Metallica".ljust(20),"isn\'t metal")
print("      Metallica".lstrip(20),"isn\'t metal")





