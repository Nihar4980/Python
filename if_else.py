
x = 12
print(f"The value of x {x}")


# task 1: Check person is eligble for voting
# task 2: Check the number is even or odd
# task 4: Login credential input sucessfully
# task 3: Find largest and smallest number in between three number
age = int(input("Enter your age :"))
if age > 0:
    if age >= 18:
        print("You are Eligble for voting")
    else:
        print("You are not Eligble for voting")
else:
    print("Enter a valid a age")

    



# task 2: Check the number is even or odd
num = int(input("Enter a number:"))
if num%2 == 0:
    print("Even number")
else: 
    print("Odd number")

if num%2 != 0:
    print("Odd number")
else: 
    print("Even number")



# task 3: Find largest and smallest number in between three number
a,b,c = int(input()), int(input()), int(input())

if a == b == c:
    print("All number are equal")
else:
    if a>b & a>c:
        print(f"{a} is greater than {b} and {c}")
        if b<c:
            print(f"{b} is smallest than {a} and {c}")
        else:
            print(f"{c} is smallest than {a} and {b}")
    elif b>a & b>c:
        print(f"{b} is greater than {a} and {c}")
        if a<c:
            print(f"{a} is smallest than {b} and {c}")
        else:
            print(f"{c} is smallest than {a} and {b}")
    else:
        print(f"{c} is greater than {a} and {b}")
        if a<b:
            print(f"{a} is smallest than {b} and {c}")
        else:
            print(f"{b} is smallest than {a} and {c}")

            

# task 4: Login credential input sucessfully
userid = str(input("Enter your userid : "))
password = str(input("Eneter your password : "))

if userid == "python" and password == "12345":
    print("login sucessfully")
else:
    print("invalid credentials")

# task 5: take a input (1-7) show day name e.g. - if 1 output Monday
days = ["sunday","monday", "tuesday", "wednesday", "thursday", "friday","saturday" ]
num = int(input())
print(f"Today is {days[num-1]}")