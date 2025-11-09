# # import sys
# # list1 = [1,2]
# # print(sys.getsizeof(list1))
# # x = iter(list1)
# # print(sys.getsizeof(x)) # it gives you memory size of varible x
# # print(next(x))
# # print(next(x))
# # print(x)
# # print(next(x))


# # task 1: make all elements of list with a 10 multiplier
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# for i in list1:
#     list2.append(i*10)
# print(list2)

# # task 2: print sum of all element of list
# sum = 0
# for i in list1:
#     sum += i
# print(sum)

# # task 3: print multiply of all element of list
# product = 1
# for i in list1:
#     product *= i
# print(product)

# # task 4: make all elements of list with a 10 multiplier in one line code
# list2 = [i*10  for i in list1]
# print(list2)

# # task 5: print all even number from list
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# for i in list1:
#     if i%2 == 0:
#         list2.append(i)
# print(list2)

# # task 6: print all even number from list using list comprenshive
# list2 = [i for i in list1 if i%2 == 0]
# print(list2)

# #task 7 Range
# for i in range(1,11):
#     print(i)

# #task 8: factorial of a num
# num = 5
# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)

# #task 9: reverse a list using for loop
# list2 = []
# for i in list1:
#     list2.insert(0,i)
# print(list2)

# # Swaping
# a, b = 5, 6
# c = b
# b = a
# a = c
# print(a,b)


# #task 10: sort a list using for loop
# list3 = [3,2,1,4,5,8,9,6,10,7]
# for i in range(len(list3)):
#     for j in range(len(list3) - i -1):
#         if list3[j] > list3[j+1]:
#             list3[j], list3[j+1] = list3[j+1], list3[j]
# print(list3)

# # add element wise of two list
# l1 = [1,2,3,4,5,6]
# l2 = [1,2,3,4,5,6]
# #output = [2,4,6,8,10,12]
# l3 = [l1[i]+l2[i] for i in range(len(l1))]
# print(l3)


# create a 5X2 matrix
x = [[1,2],[2,3],[3,4],[4,5],[5,6]]
print(x[0][0])








# Matrix multiplication 
x1 = [[1,2,3,4],[4,5,6,5],[7,8,9,6]]
x2 = [[2,5,6],[7,3,4],[2,3,5],[4,5,6]]
# rule : mxn * nxp = mxp
rows_x1 = len(x1) #3
cols_x1 = len(x1[0]) #4
rows_x2 = len(x2) # 4
cols_x2 = len(x2[0]) # 3

result = [[0 for _ in range(cols_x2)] for _ in range(rows_x1)] 

for i in range(rows_x1 ): #[0,1,2]
    for j in range(cols_x1):#[0,1,2,3]
        for k in range(cols_x2): #[0,1,2]
            result[i][k] += x1[i][j] * x2[j][k]

print(result)




# create a list that store all even number in between 1, 100 

# list_even = []
# odd_list = []
# for i in range(1,101):
#     if i%2 == 0:
#         list_even.append(i)
#     else:
#         odd_list.append(i)
# print(list_even)
# print(odd_list)


# l1 = [i for i in range(1,101) if i%2==0]
# print(l1)

