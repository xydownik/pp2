s1 ={"Pink Floyd", "Metallica", "Led Zeppelin"}
s2 = {"Placebo","Jimi Hendrix", "Metallica"}
s1.intersection_update(s2)
print(s1)

s1.intersection(s2)
print(s1)

s1.symmetric_difference_update(s2)
print(s1)

s1.symmetric_difference(s2)
print(s1)

s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)




