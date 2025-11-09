# print 1 to 10 using while loop
i = 1
while i<11:
    print(i)
    i +=1

print("*****************************")

# print 10 to 1 using while loop
i = 10
while i >=1:
    print(i)
    i -=1
print("*****************************")
#learning continue and break in while loop
i = 0
while i<10:
    i +=1
    if i == 5:
        continue
    print(i)
print("*****************************")
i = 0
while i<10:
    i +=1
    if i == 5:
        break
    print(i)
print("*****************************")
# task : revrese a list using while loop
list1 = [4,3,2,5,6,7,8,9]
print(list1)
list2 =[]
index = len(list1) -1

while index >= 0:
    list2.append(list1[index])
    index -= 1
print(list2)
print("*****************************")

list1 = [4,3,2,5,6,7,8,9]
print(list1)
start = 0
end = len(list1) -1
while start < end:
    list1[start], list1[end] = list1[end], list1[start]
    start += 1
    end -= 1   
print(list1)
print("*****************************")
# task: sort a list using while loop
    
