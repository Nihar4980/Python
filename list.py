num = [1,2,3,4,5,6,10]
print(type(num))
print(num)

floats = [1.0, 2.0, 3.5, 4.5]
print(floats)

name = ['Ram', 'Shyam', 'krishna']
print(name)


l = []
# del l
print(l)

l.append(1)
print(l)
l.append(2)
print(l)
l.append(3)
print(l)

num.append(10)
print(num)
num.append("Hi")
print(num)

l.clear()
print(l)

l1 = l.copy()
print(l1)

l.extend([1,2,3,4,5,6,7,8,9,10])
print(l)
l.extend([10,11,11,12,13])
print(l)
print(l.count(10))
print(l.count(11))
print(l.count(13))

print(l.index(13))

l.insert(0,0)
print(l)
l.insert(8,15)
print(l)
l.insert(-3,15)
print(l)

l.append([1,2,3,4])
print(l)
print(len(l))

l.pop()
print(l)

l.pop(8)
print(l)

l.remove(11)
print(l)

l.pop(0)
print(l)

l.reverse()
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

# Indexing
print(l[5])

print(l[-4])

# slicing
print(l[5:9])
print(l[3:9])
print(l[:9])
print(l[:3])
print(l[-4:])

# length
print(len(l))


marks = [45, 56, 90, 46, 78, 45]
print(marks[1])

print(marks[1:6])



