# ============================================================
# PYTHON OOP - COMPLETE BASIC NOTES
# ============================================================

# OOP = Object-Oriented Programming
#
# OOP ka use code ko classes aur objects ke form me organize
# karne ke liye hota hai.
#
# Real-world example:
# Student, Employee, Car, BankAccount etc.
#
# OOP ke important concepts:
#
# 1. Class
# 2. Object
# 3. __init__()
# 4. self
# 5. Attributes / Variables
# 6. Methods
# 7. Class Variable
# 8. Instance Variable
# 9. Inheritance
# 10. Polymorphism
# 11. Encapsulation
# 12. Abstraction


# ============================================================
# 1. CLASS
# ============================================================

# Class = Blueprint / Design
#
# Example:
# Student ek class hai.
#
# Class ke andar hum data aur functions define kar sakte hain.


class Student:
    pass


# ============================================================
# 2. OBJECT
# ============================================================

# Object = Class se bana actual item.
#
# Student class se student1 object banaya.

student1 = Student()

print(student1)


# Simple memory:
#
# Class  = Blueprint
# Object = Blueprint se bana actual object


# ============================================================
# 3. __init__()
# ============================================================

# __init__() ek special method hai.
#
# Jab object create hota hai tab __init__() automatically run hota hai.
#
# Iska common use object ke andar starting data set karna hai.


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Maruf", 25)

print(student1.name)
print(student1.age)


# Output:
# Maruf
# 25


# ============================================================
# 4. self
# ============================================================

# self = current object
#
# Jab student1 object ka data use ho raha hai,
# self student1 ko refer karega.
#
# Jab student2 object ka data use hoga,
# self student2 ko refer karega.


class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Maruf")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)


# Output:
# Maruf
# Rahul


# Easy memory:
#
# self = current object


# ============================================================
# 5. INSTANCE VARIABLE
# ============================================================

# Object ke andar jo variable hota hai usko
# Instance Variable bolte hain.
#
# Usually self.variable ke through banate hain.


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Maruf", 25)
student2 = Student("Rahul", 22)

print(student1.name)
print(student2.name)


# name aur age yaha instance variables hain.
#
# Har object ka apna data ho sakta hai.


# ============================================================
# 6. METHOD
# ============================================================

# Class ke andar banaya gaya function = Method


class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Maruf")

student1.introduce()


# Output:
# My name is Maruf


# ============================================================
# 7. METHOD WITH PARAMETERS
# ============================================================

class Calculator:

    def add(self, a, b):
        print(a + b)


calc = Calculator()

calc.add(10, 20)


# Output:
# 30


# ============================================================
# 8. METHOD WITH RETURN
# ============================================================

class Calculator:

    def add(self, a, b):
        return a + b


calc = Calculator()

result = calc.add(10, 20)

print(result)


# Output:
# 30


# ============================================================
# 9. MULTIPLE OBJECTS
# ============================================================

# Ek class se multiple objects bana sakte hain.


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Maruf", 25)
student2 = Student("Aman", 23)
student3 = Student("Rahul", 22)

student1.introduce()
student2.introduce()
student3.introduce()


# Har object ka data different ho sakta hai.


# ============================================================
# 10. CLASS VARIABLE
# ============================================================

# Class Variable = class ke andar common variable.
#
# Iska same value normally sab objects ke liye hota hai.


class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name


student1 = Student("Maruf")
student2 = Student("Rahul")

print(student1.name)
print(student1.college)

print(student2.name)
print(student2.college)


# Output:
# Maruf
# ABC College
# Rahul
# ABC College


# Easy difference:
#
# Instance Variable:
# Har object ka different data.
#
# Class Variable:
# Sab objects ke liye common data.


# ============================================================
# 11. INSTANCE VARIABLE VS CLASS VARIABLE
# ============================================================


class Student:

    college = "ABC College"       # Class Variable

    def __init__(self, name):
        self.name = name          # Instance Variable


student1 = Student("Maruf")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)

print(student1.college)
print(student2.college)


# name -> different for each object
# college -> common


# ============================================================
# 12. INHERITANCE
# ============================================================

# Inheritance = Ek class dusri class ke
# properties/methods use kar sakti hai.
#
# Parent Class = Base Class
# Child Class = Derived Class
#
# Example:
#
# Animal = Parent
# Dog = Child


class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.bark()


# Output:
# Animal is eating
# Dog is barking


# Dog ne Animal ka eat() method inherit kiya.


# ============================================================
# 13. INHERITANCE WITH __init__()
# ============================================================


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def study(self):
        print(self.name, "is studying")


student1 = Student("Maruf")

print(student1.name)
student1.study()


# Output:
# Maruf
# Maruf is studying


# Student class ne Person ka __init__() use kiya.


# ============================================================
# 14. METHOD OVERRIDING
# ============================================================

# Child class parent ke method ko apne according
# redefine kar sakti hai.
#
# Isko Method Overriding bolte hain.


class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()


# Output:
# Dog barks


# Parent ka sound() method tha.
# Child ne usko apne version se replace kar diya.


# ============================================================
# 15. POLYMORPHISM
# ============================================================

# Polymorphism = "Many Forms"
#
# Same method name different classes me
# different behavior de sakta hai.


class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# Output:
# Dog barks
# Cat meows


# Same method:
# sound()
#
# Lekin output different.


# ============================================================
# 16. ENCAPSULATION
# ============================================================

# Encapsulation = Data aur methods ko ek class ke andar
# combine karke rakhna.
#
# Simple example:


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount(10000)

account.show_balance()


# Data aur method ek hi class ke andar hain.


# ============================================================
# 17. PRIVATE VARIABLE - BASIC IDEA
# ============================================================

# Python me __variable likhne par hum usko
# private-style variable bana sakte hain.
#
# Example:


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(10000)

account.show_balance()


# Output:
# Balance: 10000


# Directly:
#
# print(account.__balance)
#
# Normally access nahi kar sakte.


# ============================================================
# 18. ABSTRACTION
# ============================================================

# Abstraction = Unnecessary internal details hide karna
# aur user ko sirf important functionality dikhana.
#
# Real-life example:
#
# Car start karne ke liye hum sirf button press karte hain.
# Engine ke andar exactly kya ho raha hai,
# user ko sab details pata hona zaroori nahi.


# Simple programming example:


class Car:

    def start(self):
        self.__engine_start()
        print("Car started")

    def __engine_start(self):
        print("Engine started")


car = Car()

car.start()


# User ko sirf:
#
# car.start()
#
# pata hona chahiye.
#
# Internal __engine_start() kaise kaam karta hai,
# wo hide kiya gaya hai.


# ============================================================
# 19. COMPLETE OOP EXAMPLE
# ============================================================

class Employee:

    company = "ABC Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)


employee1 = Employee("Maruf", 25000)
employee2 = Employee("Rahul", 30000)

employee1.show_details()
print()

employee2.show_details()


# ============================================================
# 20. OOP MOST IMPORTANT TERMS
# ============================================================

# Class
# -> Blueprint / design
#
# Object
# -> Class ka actual instance
#
# __init__()
# -> Object create hone par automatically run hota hai
#
# self
# -> Current object
#
# Attribute
# -> Object/class ka data
#
# Method
# -> Class ke andar function
#
# Instance Variable
# -> Har object ka apna data
#
# Class Variable
# -> Common data
#
# Inheritance
# -> Parent class se features lena
#
# Polymorphism
# -> Same method, different behavior
#
# Encapsulation
# -> Data aur methods ko class me combine karna
#
# Abstraction
# -> Unnecessary details hide karna


# ============================================================
# 21. VERY IMPORTANT MEMORY TRICK
# ============================================================

# OOP ko is order me yaad karo:
#
# Class
#    ↓
# Object
#    ↓
# __init__
#    ↓
# self
#    ↓
# Variables
#    ↓
# Methods
#    ↓
# Inheritance
#    ↓
# Polymorphism
#    ↓
# Encapsulation
#    ↓
# Abstraction


# ============================================================
# 22. REAL-WORLD EXAMPLE
# ============================================================

# Class = Employee
#
# Objects:
# employee1
# employee2
#
# Data:
# name
# salary
# department
#
# Methods:
# work()
# show_details()
#
# Ye OOP ka basic real-world structure hai.


class Employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def work(self):
        print(self.name, "is working")

    def show_details(self):
        print("Name:", self.name)
        print("Department:", self.department)


employee1 = Employee("Maruf", "HR")

employee1.show_details()
employee1.work()


# ============================================================
# FINAL QUICK REVISION
# ============================================================

# 1. OOP
# Object-Oriented Programming.
#
# 2. Class
# Blueprint.
#
# 3. Object
# Class ka actual instance.
#
# 4. __init__
# Object create hote time automatically run hota hai.
#
# 5. self
# Current object.
#
# 6. Method
# Class ke andar function.
#
# 7. Instance Variable
# Object-specific data.
#
# 8. Class Variable
# Common data.
#
# 9. Inheritance
# Parent se features lena.
#
# 10. Polymorphism
# Same method, different behavior.
#
# 11. Encapsulation
# Data + methods ko class ke andar rakhna.
#
# 12. Abstraction
# Unnecessary details hide karna.


# ============================================================
# OOP ONE-LINE MEMORY
# ============================================================

# Class = Blueprint
# Object = Actual thing
# __init__ = Starting data
# self = Current object
# Method = Action
# Inheritance = Parent se lena
# Polymorphism = Different behavior
# Encapsulation = Data ko protect/organize karna
# Abstraction = Details hide karna