# class Student:
#     def __init__(self,name, age, marks,subject, roll):
#             self.name = name
#             self.age = age
#             self.marks = marks
#             self.subject = subject
#             self.roll = roll
#     def show(self):
#           print(f"Name = {self.name}")
#           print(f"Age = {self.age}")
#           print(f"Marks = {self.marks}")
#           print(f"Subject = {self.subject}")
#           print(f"Roll = {self.roll}")
          

# s1 = Student("WPU",25,97,"Python",20)
# s2 = Student("MIT",20,90,"Python",21)
# print(s1.show())
# print(s2.show())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def multi(self):
        return self.a*self.b
    
    def div(self):
        return self.a/self.b
    
    def round(self):
        return self.a//self.b
    
m1 = Math(10,3)
print(m1.add())
print(m1.sub())
print(m1.multi())
print(m1.div())
print(m1.round())

pi = 3.14
class Area:
    def __init__(self,radius, side, base, height,length, width):
        self.radius = radius
        self.side = side
        self.base = base
        self.height = height
        self.length = length
        self.width = width
        global pi
    def circle(self):
        return pi * self.radius**2

    def square(self):
        return  self.side**2
    
    def rectangle(self):
        return self.width * self.length
    
    def triangle(self):
        return 0.5 * self.height * self.base
    
    def sphere(self):
        return (4/3) * pi * self.radius**3   
    
a1 = Area(3,4,5,6,7,8)
print(a1.circle())
print(a1.square())
print(a1.rectangle())
print(a1.triangle())
print(a1.sphere())





