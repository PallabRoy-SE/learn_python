# unordered and unique

s1 = {1, 2, 4, 7}  # {1, 2, 4, 7}
s2 = {3, 2, 1, 3, 6}  # {1, 2, 3, 6}

print(s1, s2)

s1.add(9)
print(s1)
s1.remove(9)
print(s1)
s1.discard(9)  # don't throw error if item not present in set
s1.pop()  # remove randomly

print(s1)

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
