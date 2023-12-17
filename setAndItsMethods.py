s=set()
print(type(s))
s1={1,2,3,4,5}
s2={4,5,6,7,1}

print(s1.union(s2))

s1.update(s2)
print(s1)

print(s1.intersection(s2))

print(s1.symmetric_difference(s2))

print(s1.difference(s2))

print(s1.isdisjoint(s2))

print(s1.issuperset(s2))

print(s1.issubset(s2))

s1.remove(1)
s1.discard(1)
s1.pop()
print(s1)

s1.add("Hey")
print(s1)

s1.clear()
print(s1)

del s2
