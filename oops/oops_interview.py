# ============================================================
# PYTHON OOP - MNC INTERVIEW QUESTIONS & ANSWERS
# ============================================================

# NOTE:
# Answers are in simple English.
# Learn the meaning, not only the exact words.


# ============================================================
# Q1. What is OOP?
# ============================================================

# Answer:
# OOP stands for Object-Oriented Programming.
# It is a way of writing programs using classes and objects.


# ============================================================
# Q2. Why do we use OOP?
# ============================================================

# Answer:
# OOP helps us organize code.
# It also helps us reuse and maintain code.


# ============================================================
# Q3. What is a class?
# ============================================================

# Answer:
# A class is a blueprint for creating objects.


# ============================================================
# Q4. What is an object?
# ============================================================

# Answer:
# An object is an instance of a class.


# ============================================================
# Q5. What is the difference between class and object?
# ============================================================

# Answer:
# A class is a blueprint.
# An object is the actual instance created from a class.


# ============================================================
# Q6. What is __init__()?
# ============================================================

# Answer:
# __init__() is a special method.
# It runs automatically when an object is created.
# It is used to set initial data.


# ============================================================
# Q7. What is self?
# ============================================================

# Answer:
# self refers to the current object.
# It is used to access object data and methods.


# ============================================================
# Q8. Is self a keyword in Python?
# ============================================================

# Answer:
# No, self is not a Python keyword.
# It is the common name used for the current object.


# ============================================================
# Q9. What is a method?
# ============================================================

# Answer:
# A method is a function defined inside a class.


# ============================================================
# Q10. What is an attribute?
# ============================================================

# Answer:
# An attribute is data stored in an object or class.


# ============================================================
# Q11. What is an instance variable?
# ============================================================

# Answer:
# An instance variable belongs to an object.
# Different objects can have different values.


# Example:

class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Maruf")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)


# ============================================================
# Q12. What is a class variable?
# ============================================================

# Answer:
# A class variable is shared by the objects of a class.


# Example:

class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name


student1 = Student("Maruf")
student2 = Student("Rahul")

print(student1.college)
print(student2.college)


# ============================================================
# Q13. Instance variable vs class variable?
# ============================================================

# Answer:
# Instance variable belongs to each object.
# Class variable is shared by the class objects.


# ============================================================
# Q14. What is inheritance?
# ============================================================

# Answer:
# Inheritance allows a child class to use
# the features of a parent class.


# Example:

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


# ============================================================
# Q15. Why do we use inheritance?
# ============================================================

# Answer:
# We use inheritance to reuse code
# and reduce duplicate code.


# ============================================================
# Q16. What is a parent class?
# ============================================================

# Answer:
# A parent class is the class from which
# another class gets its features.


# ============================================================
# Q17. What is a child class?
# ============================================================

# Answer:
# A child class is a class that gets features
# from a parent class.


# ============================================================
# Q18. What is method overriding?
# ============================================================

# Answer:
# Method overriding means a child class creates
# its own version of a parent class method.


# Example:

class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()


# ============================================================
# Q19. What is polymorphism?
# ============================================================

# Answer:
# Polymorphism means the same method
# can have different behavior.


# Example:

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


# ============================================================
# Q20. What is encapsulation?
# ============================================================

# Answer:
# Encapsulation means keeping data and methods
# together inside a class.


# ============================================================
# Q21. What is abstraction?
# ============================================================

# Answer:
# Abstraction means hiding unnecessary details
# and showing only important information.


# ============================================================
# Q22. What are the four pillars of OOP?
# ============================================================

# Answer:
# The four main pillars are:
#
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction


# ============================================================
# Q23. Is Python an OOP language?
# ============================================================

# Answer:
# Yes, Python supports Object-Oriented Programming.


# ============================================================
# Q24. Can we create multiple objects from one class?
# ============================================================

# Answer:
# Yes.
# We can create multiple objects from one class.


# ============================================================
# Q25. Can different objects have different values?
# ============================================================

# Answer:
# Yes.
# Each object can have its own values.


# ============================================================
# Q26. Can a child class use parent class methods?
# ============================================================

# Answer:
# Yes.
# A child class can use parent methods through inheritance.


# ============================================================
# Q27. What is the difference between function and method?
# ============================================================

# Answer:
# A function can be outside a class.
# A method is a function inside a class.


# ============================================================
# Q28. What is code reusability?
# ============================================================

# Answer:
# Code reusability means using existing code again
# instead of writing the same code again.


# ============================================================
# Q29. What is a private variable?
# ============================================================

# Answer:
# A private variable is used to restrict direct access
# to data from outside the class.
#
# In Python, we commonly use __ before the variable name.


# Example:

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)


account = BankAccount(10000)

account.show_balance()


# ============================================================
# Q30. What happens when we create an object?
# ============================================================

# Answer:
# Python creates the object.
# Then __init__() runs automatically if it is defined.


# ============================================================
# MNC CODING QUESTIONS
# ============================================================


# ============================================================
# Coding Q1. Create a Student class
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


student = Student("Maruf", 25)

student.show_details()


# ============================================================
# Coding Q2. Create an Employee class
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee = Employee("Maruf", 25000)

employee.show_details()


# ============================================================
# Coding Q3. Create a Calculator class
# ============================================================

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))


# ============================================================
# Coding Q4. Demonstrate inheritance
# ============================================================

class Person:

    def introduce(self):
        print("I am a person")


class Student(Person):

    def study(self):
        print("I am studying")


student = Student()

student.introduce()
student.study()


# ============================================================
# Coding Q5. Demonstrate method overriding
# ============================================================

class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()


# ============================================================
# Coding Q6. Demonstrate polymorphism
# ============================================================

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


# ============================================================
# Coding Q7. Bank Account
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount(10000)

account.show_balance()

account.deposit(5000)

account.show_balance()


# ============================================================
# MOST IMPORTANT QUESTIONS TO MEMORIZE
# ============================================================

# 1. What is OOP?
# 2. What is a class?
# 3. What is an object?
# 4. What is __init__()?
# 5. What is self?
# 6. What is a method?
# 7. What is inheritance?
# 8. What is polymorphism?
# 9. What is encapsulation?
# 10. What is abstraction?
# 11. What are the four pillars of OOP?
# 12. Instance variable vs class variable?
# 13. What is method overriding?
# 14. Why do we use OOP?
# 15. What is code reusability?


# ============================================================
# EASY 1-LINE REVISION
# ============================================================

# Class       = Blueprint
# Object      = Instance of class
# __init__    = Sets initial data
# self        = Current object
# Method      = Function inside class
# Inheritance = Reuse parent class features
# Polymorphism = Same method, different behavior
# Encapsulation = Data + methods together
# Abstraction = Hide unnecessary details