s1 ={"Pink Floyd", "Metallica", "Led Zeppelin","Pink Floyd"}
s2 = {"Placebo","Jimi Hendrix"}

s2.add("Metallica")
print(s2)

s3 = s2.copy()
print(s3)

s3.clear()
print(s3)

print(s1.difference(s2))

s1.difference_update(s2)
print(s1)

s2.discard("Metallica")
print(s2)

s2.update({"Pink Floyd"})
print(s2)

print(s1.intersection(s2))

s1.intersection_update(s2)

print(s1)

s1 ={"Pink Floyd", "Metallica", "Led Zeppelin","Pink Floyd"}
s2 = {"Pink Floyd","Metallica"}

print(s2.issubset(s1))

print(s1.isdisjoint(s2))

print(s1.issuperset(s2))

print(s1.symmetric_difference(s2))

s1.symmetric_difference_update(s2)
print(s1)


print(s1.union(s2))

s1.update(s2)
print(s1)


