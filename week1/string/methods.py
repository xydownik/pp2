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
print(21," & ".join(f))
print("Metallica".ljust(20),"isn\'t metal")
print(22, "      Metallica".lstrip(),"isn\'t metal")
m= t.maketrans("F", "L")
print(23, t.translate(m))
print(24, "Jimi Hendrix Experience".partition("Hendrix"))
print(25, t.replace("Floyd", "Anderson"))
print("26-27",  "Your mom, my mom".rfind("mom"), "Your mom, my mom".rindex("mom"))
print(28, t.rjust(20))
print(29, "Jimi Hendrix Experience is Jimi Hendrix\'s group".rpartition("Jimi"))
print(30,"Metallica,Pink Floyd,B.B.King".rsplit(","))
print(31,"Pink Floyd      ".rstrip(),": THE WALL")
print(32,"Metallica PinkFloyd B.B.King".split())
print(33,"Metallica PinkFloyd\nB.B.King".splitlines())
print(34,t.startswith("P"))
print(35,"In psychedelics,","     Pink Floyd    ".strip(),"is my favorite one")
print(36, t.swapcase())
print(37, "pink floyd".title())
print(38, t.translate({105:117}))
print(39,"the wall".upper())
print(40, " 10".zfill(20))






