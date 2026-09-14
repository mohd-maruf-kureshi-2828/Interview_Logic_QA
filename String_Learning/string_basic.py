# ==========================================
# PYTHON STRINGS - BASICS
# ==========================================


# What is a String?
# A string is a collection of characters/text.
# Example:

name = "Maruf"
city = "Bengaluru"

print(name)
print(city)


# We can create a string using single quotes or double quotes.

name1 = "Maruf"
name2 = 'Maruf'

print(name1)
print(name2)


# String Indexing
# Index means position of a character.
# Python indexing starts from 0.

name = "Maruf"

print(name[0])  # M
print(name[1])  # a
print(name[2])  # r
print(name[3])  # u
print(name[4])  # f


# Negative Indexing
# -1 means last character.
# -2 means second last character.

print(name[-1])  # f
print(name[-2])  # u


# String Length
# len() returns the number of characters in a string.

print(len(name))  # 5


# String Slicing
# Slicing is used to get a part of a string.
# Syntax: string[start:end]
# The end index is not included.

print(name[0:3])  # Mar
print(name[1:4])  # aru


# Important:
# String indexing starts from 0.
# String slicing end index is excluded.


# Strings are Immutable
# Immutable means we cannot directly change an existing string character.

name = "Maruf"

# This will give an error:
# name[0] = "K"

# Instead, we create a new string.

name = "Karuf"

print(name)


# String Concatenation
# Concatenation means joining two or more strings.

first_name = "Mohamed"
last_name = "Maruf"

full_name = first_name + " " + last_name

print(full_name)


# String Repetition
# We can repeat a string using *.

word = "Hi "

print(word * 3)


# Checking String Type

name = "Maruf"

print(type(name))

# Output:
# <class 'str'>


# ==========================================
# INTERVIEW QUESTIONS
# ==========================================


# Q1. What is a string in Python?
#
# Interview Answer:
# A string is a collection of characters used to store text data.


# Q2. How do you create a string in Python?
#
# Interview Answer:
# We can create a string using single quotes or double quotes.
#
# Example:
# name = "Maruf"
# name = 'Maruf'


# Q3. What is string indexing?
#
# Interview Answer:
# String indexing is used to access individual characters
# from a string. Python indexing starts from 0.


# Q4. What is negative indexing?
#
# Interview Answer:
# Negative indexing is used to access characters from the end
# of a string. -1 represents the last character.


# Q5. What is string slicing?
#
# Interview Answer:
# String slicing is used to extract a part of a string.
#
# Example:
# name[0:3]


# Q6. Are strings mutable or immutable?
#
# Interview Answer:
# Strings are immutable in Python.
# It means we cannot directly change an existing string.


# Q7. What is concatenation?
#
# Interview Answer:
# Concatenation means joining two or more strings together.
#
# Example:
# "Hello" + " World"


# Q8. Which function is used to find the length of a string?
#
# Interview Answer:
# The len() function is used to find the length of a string.
#
# Example:
# len("Maruf")
# Output: 5