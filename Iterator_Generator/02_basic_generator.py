# ============================================================
# PYTHON ITERATORS & GENERATORS - BASIC NOTES
# ============================================================


# ============================================================
# 1. ITERATOR KYA HAI?
# ============================================================

# Iterator ek object hai jo values ko
# ek-ek karke deta hai.
#
# Python me iter() aur next() se iterator bana/use kar sakte hain.


numbers = [10, 20, 30]

my_iterator = iter(numbers)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Output:
# 10
# 20
# 30


# ============================================================
# 2. iter()
# ============================================================

# iter() kisi iterable object se iterator banata hai.


numbers = [1, 2, 3]

my_iterator = iter(numbers)

print(my_iterator)


# ============================================================
# 3. next()
# ============================================================

# next() iterator se next value deta hai.


numbers = [10, 20, 30]

my_iterator = iter(numbers)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


# Output:
# 10
# 20
# 30


# Agar available values khatam ho jaye
# aur next() dobara use karein,
# StopIteration error aa sakta hai.


# ============================================================
# 4. FOR LOOP AND ITERATOR
# ============================================================

# for loop internally iterator ka concept use karta hai.


numbers = [10, 20, 30]

for number in numbers:
    print(number)


# Output:
# 10
# 20
# 30


# Beginner ke liye:
# for loop use karna normally easier hai.
# Har jagah manually iter() aur next() use karne ki zarurat nahi.


# ============================================================
# 5. ITERABLE VS ITERATOR
# ============================================================

# Iterable:
# Jis object ko hum loop kar sakte hain.
#
# Examples:
# list
# tuple
# string
# dictionary
# set
#
# Iterator:
# Jo values ko ek-ek karke deta hai.


numbers = [10, 20, 30]

# numbers = iterable

my_iterator = iter(numbers)

# my_iterator = iterator


# Easy memory:
#
# Iterable -> Can be looped
# Iterator -> Gives values one by one


# ============================================================
# 6. GENERATOR
# ============================================================

# Generator bhi values ko ek-ek karke deta hai.
#
# Generator banane ke liye function ke andar
# yield keyword use karte hain.


def numbers():
    yield 1
    yield 2
    yield 3


result = numbers()

print(next(result))
print(next(result))
print(next(result))


# Output:
# 1
# 2
# 3


# ============================================================
# 7. yield KYA HAI?
# ============================================================

# yield value ko ek-ek karke return karta hai.
#
# Normal return function ko finish kar deta hai.
# yield function ko temporarily pause karta hai.


def demo():
    yield 10
    yield 20
    yield 30


result = demo()

print(next(result))
print(next(result))
print(next(result))


# Output:
# 10
# 20
# 30


# ============================================================
# 8. GENERATOR WITH FOR LOOP
# ============================================================


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4


for number in numbers():
    print(number)


# Output:
# 1
# 2
# 3
# 4


# ============================================================
# 9. NORMAL FUNCTION VS GENERATOR
# ============================================================


# Normal function:

def normal_function():
    return [1, 2, 3, 4, 5]


print(normal_function())


# Generator:

def generator_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for number in generator_function():
    print(number)


# ============================================================
# 10. WHY USE GENERATORS?
# ============================================================

# Generator values ko ek-ek karke deta hai.
#
# Isliye large data ke saath memory save kar sakta hai.


def numbers():
    for i in range(1, 6):
        yield i


for number in numbers():
    print(number)


# ============================================================
# 11. SIMPLE REAL-WORLD EXAMPLE
# ============================================================

# Socho 1 lakh records hain.
#
# Agar hum saare records ek saath memory me load karein,
# memory zyada use ho sakti hai.
#
# Generator records ko ek-ek karke process kar sakta hai.


def data():
    for i in range(1, 6):
        yield i


for item in data():
    print("Processing:", item)


# ============================================================
# 12. ITERATOR VS GENERATOR
# ============================================================

# Iterator:
# Object jo values ko one by one deta hai.
#
# Generator:
# Easy way to create an iterator using yield.


# Easy memory:
#
# Iterator -> One by one values
# Generator -> yield se one by one values


# ============================================================
# 13. IMPORTANT INTERVIEW DEFINITIONS
# ============================================================

# Iterator:
# An iterator is an object that gives values one by one.
#
# Generator:
# A generator is a simple way to create an iterator
# using the yield keyword.
#
# yield:
# yield gives a value and pauses the function temporarily.
#
# iter():
# iter() creates an iterator from an iterable.
#
# next():
# next() gets the next value from an iterator.


# ============================================================
# FINAL MEMORY
# ============================================================

# Iterable
#    ↓
# Can be looped
#
# Iterator
#    ↓
# Gives values one by one
#
# Generator
#    ↓
# Creates an iterator using yield


# ============================================================
# IMPORTANT
# ============================================================

# Fresher interview ke liye abhi itna enough hai.
#
# Advanced iterator protocols aur complex generators
# abhi nahi karne hain.