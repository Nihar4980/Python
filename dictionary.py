student = {"roll":[1,2,3,4,5,6,7,8,9,10],'Marks':[34,12,12,23,12,56,78,90,99,96]}

print(student)
print(student.items())
print(student.keys())
print(student.values())
print(student['roll'])
print(student['Marks'])
# q-1: change marks 99 to 9 if any avilable ?
print(type(student['Marks']))
index_99 = student['Marks'].index(99)
student['Marks'][index_99] = 9
print(student['Marks'])

print(list(student.values())[0])

s3 = {0:10, 1: 20} # out_put = {0:10, 1: 20, 2:addition s1.keys[0], s.keys[1]}
#s3.update({2:30})
#s3[2] = 30
s3[2] = s3[0] + s3[1]
print(s3)

