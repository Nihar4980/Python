# | Term                         | Description                                        |
# | ---------------------------- | -------------------------------------------------- |
# | **Class**                    | A blueprint or template for creating objects.      |
# | **Object**                   | An instance of a class. It contains real data.     |
# | **Method**                   | A function defined inside a class.                 |
# | **Attribute**                | Variables stored inside a class/object.            |
# | **Constructor (`__init__`)** | A special method used to initialize object values. |


# A. Encapsulation
#   - Wrapping data (variables) and methods (functions) inside a class and restricting access to some of the object's components.

class Person:
    def __init__(self, name, age):
        self.name = name        # public variable
        self._age = age         # protected variable
        self.__salary = 50000   # private variable

    def display(self):
        return self.__salary

    def show(self):
        print(self.name, self._age)

p = Person("John", 30)
print(p.name)          # Accessible
print(p._age)          # Accessible but not recommended
#print(p.__salary)    # Not accessible (private)
print(p.display())

class Person:
    def __init__(self, name, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age")

p = Person("John", 25)
print(p.get_age())     # 25
p.set_age(30)
print(p.get_age()) 

# B. Inheritance

# Allows one class (child) to use properties and methods of another class (parent).

class Animal:
    def speak(self):
        return "Animal speaks"

# Single Inheritance
class Dog(Animal):
    def bark(self):
        return "Dog barks"

dog = Dog()
print(dog.speak(), dog.bark())

# Types of Inheritance:
# Type	           Description
# Single	    One parent → one child
# Multiple	    One child → multiple parents
# Multilevel	Grandparent → Parent → Child
# Hierarchical	One parent → multiple children
# Hybrid	    Combination of different types

# Single Inheritance

# ✔ One parent → one child

class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


# 2️⃣ Multilevel Inheritance

# ✔ Grandparent → Parent → Child

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.speak()
p.bark()
p.weep()



# 3️⃣ Multiple Inheritance

# ✔ One child → multiple parents

class Father:
    def skill(self):
        print("Father can drive")

class Mother:
    def quality(self):
        print("Mother is caring")

class Child(Father, Mother):
    def hobby(self):
        print("Child loves painting")

c = Child()
c.skill()
c.quality()
c.hobby()

# 4️⃣ Hierarchical Inheritance

# ✔ One parent → multiple children

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.speak()
d.bark()
c.speak()
c.meow()



# 5️⃣ Hybrid Inheritance

# ✔ Combination of more than one type of inheritance

# Example: Hierarchical + Multiple Inheritance

class A:
    def classA(self):
        print("Class A")

class B(A):
    def classB(self):
        print("Class B (inherits A)")

class C(A):
    def classC(self):
        print("Class C (inherits A)")

class D(B, C):  # Multiple Inheritance
    def classD(self):
        print("Class D (inherits B & C)")

obj = D()
obj.classA()
obj.classB()
obj.classC()
obj.classD()




#✅ 6️⃣ Using super() in Inheritance

class Parent:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def shows(self):
        print(self.name)
        print(self.age)
c = Child("John",30)
c.shows()

class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent class constructor
        super().__init__(name)
        self.breed = breed
        print("Dog constructor called")

    def speak(self):
        # Call parent class speak() method
        super().speak()
        print(f"{self.name} barks")

# Create object
d = Dog("Tommy", "Labrador")
d.speak()

# ✅ C. Polymorphism

# Same function name but different behaviors.

# Example 1: Method Overriding (Run-time Polymorphism)

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()

# Example 2:
class Parent:
    def name(self):
        print("This is Parent's Name method")

class Child(Parent):
    def name(self):
        # Call parent class method using super()
        super().name()
        print("This is Child's Name method")

# Create object of Child class
c = Child()
c.name()

# ✅ D. Abstraction

# Hiding internal implementation and showing only necessary details.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

c = Car()
c.start()


class Student:
    college = "MIT"

    @classmethod
    def change_school(cls, name):
        cls.college = name

Student.change_school("MIT_WPU")
print(Student.college)

class Math:

    @staticmethod
    def add(arg1, arg2):
        return arg1 + arg2
m1 = Math()
print(m1.add(12, 13))
