set1 = {1,2,3,4,5,5}
print(set1)
set2 = {5,4,3,2,1}
print(set2)

# opertion
s1 = {1,2,3,4,5,6,7}
s2 = {4,5,6,7,8,9,10}
s1.add(0)
s1.add(-1)
s1.remove(-1)

print(s1)
s1.pop()
print(s1)

s1.update(s2)
print(s1)

# Mathmetical operation of set
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.symmetric_difference(s2))

