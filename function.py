# addition
def addition(x,y):
    add = x+y
    #print(add)
    return add

f = addition(1,2)
print(f)

#create a fun to calculate (a+b)^2
def whole_square(a,b):
    output = a**2 + b**2 + 2*a*b
    return output
f1 = whole_square(10,10)
print(f1)

def square(x):
    """
    creater: Your name  
    Date: 17/10/2025
    input : x -> int/
    operation: square
    output : x**2
    """
    return x**2

f2 = square(10)
print(f2)


# Arguments

def add(*args):
    return sum(args)

f = add(1,2,3,4,5,6)
print(f)

def multi(*args):
    prod = 1
    for i in args:
        prod *= i

    return prod
f = multi(1,2,3,4,5)
print(f)
# create a function to calculate average random numbers
def avg(*args):
    return sum(args)/len(args)
f = avg(1,2,3,4,5,6,7,8,9,10)
print(f)

# Keyward arguments
def key_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    return 0
f = key_print(college="MIT", subject = "Python")
print(f)


# def key_print(dict):
#     index = dict[marks].index(max(dict[marks]))
#     return dict[roll][index]
        
# dict = {'roll':[i for i in range(1,21)], 
#               'marks': [11,56,23,34,54,67,89,98,34,77,45,23,46,89,90,45,76,99,34,32]}
# f = key_print(dict)
# print(f)
# create a function which will reverse a list
def rev(list1):
    list1.reverse()
    return list1
f = rev([1,2,3,4,5,6])
print(f)

# Lambda function
sqr = lambda x: x**2
print(sqr(5))

# addition of two value using lambda function
add = lambda x,y: x+y
print(add(4,5))

# check a number is even or odd using lambda function
even_odd_check = lambda x: "even" if x%2 == 0  else "odd"
print(even_odd_check(10))

# map function
list1 = [1,2,3,4,5,6,7,8,9,10]
square_value = list(map(lambda x: x**2,list1))
print(square_value)

# filter function
list1 = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x%2==0, list1))
print(even)

odd = list(filter(lambda x: x%2!=0, list1))
print(odd)


for index, value in enumerate(list1):
    print(index, value)

list1 = [1,2,3,4,5,6,7]
list2 = [4,5,6,7,3,2,1]

list3 = [i+j for i,j in zip(list1, list2)]
print(list3)

def fun(x,y):
    return x+y,x-y, x*y, x/y

add, sub, mul, div = fun(10,2)
print(add, sub, mul, div)

_, _, mul, _ = fun(20,2)
print(mul)



# recurssion
# Find factorial of a number

def fact(n) -> int:
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

f = fact(5)
print(f)

def factor(n) -> int:
    if n == 0 or n==1:
        return 1
    else:
        return n * factor(n-1)
f = factor(6)
print(f)

