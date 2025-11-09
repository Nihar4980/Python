a = 10
print(id(a)) # memory location
print(type(a)) # datatype

# str
x = "123@#A-Z,a-z"
print(type(x))


# Numeric: int, float, complex
# int = -inf to inf
# float = all decimal 
# Complex = a + ib

# Arithmetic opertor
a, b  = 10, 15
print(a+b) # Addition
print(a-b) # Substraction
print(a*b) # Multiplication
print(a/b) # Division
print(a//b) # Rounding a decimal
print(a%b) # Reminder of division

print("*******************************")
# Float
a, b  = 10.6, 15.7
print(a+b) # Addition
print(a-b) # Substraction
print(a*b) # Multiplication
print(a/b) # Division
print(a//b) # Rounding a decimal
print(a%b) # Reminder of division

print("*******************************")
a, b  = 4 + 5j, 4 -5j # 16 - j^2 *25
print(a+b) # Addition
print(a-b) # Substraction
print(a*b) # Multiplication
print(a/b) # Division
# print(a//b) # Rounding a decimal
# print(a%b) # Reminder of division

# Assignment Operator
x = 10
x += 5  #x = x + 5
print(x)
x -= 5
print(x)
x *= 5
print(x)
x /= 5
print(x)
x **= 5
print(x)
x //= 5
print(x)

# Comparision Operator
y, z = 10, 15

print(y == z)
print(y != z)
print(y < z)
print(y > z)
print(y <= z)
print(y >= z)

# logical Operator
x,y = 10, 12
print(x<20 or y>50)
print(not(x<=10 and y>=12))

#  Identity Operators
x = 10 
y = x
print(id(x),id(y))
print(x is y)
x, y = 10,10
print(x is y)

# logical operator
x, y = 10, 15
print(x & y) # 10
print(x | y) # 15
print(x ^ y) # 5
print(x << 2) # 40
print(x >> 2) # 2
print(y << 2) # 60
print(y >> 2) # 3
