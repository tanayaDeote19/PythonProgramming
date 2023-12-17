l = [1, 2, 4, 9, 5, 1, 0, 6]

l.append("tanaya")
print(l)

l.remove("tanaya")
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(5))
print(l.copy())
print(l.count(1))
print(l.pop(6))

m = [1, 2, 3, 4]
print(l.extend(m))

#or
k=l+m
print(k)

l.insert("HEY")
print(l)

