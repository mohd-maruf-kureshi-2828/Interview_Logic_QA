# ==========================================
# PYTHON LIST - BASICS
# ==========================================


# What is a List?
#
# A list is a collection of multiple values
# stored in a single variable.
#
# Lists are:
# 1. Ordered
# 2. Mutable
# 3. Allow duplicate values
# 4. Can store different data types


numbers = [10, 20, 30, 40]

print(numbers)

# Output:
# [10, 20, 30, 40]


# ------------------------------------------
# List Indexing
# ------------------------------------------

# List indexing starts from 0.

fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

# Output:
# Apple
# Banana
# Mango


# Negative indexing

print(fruits[-1])

# Output:
# Mango


# ------------------------------------------
# List Slicing
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])

# Output:
# [10, 20, 30]


print(numbers[2:])

# Output:
# [30, 40, 50]


# ------------------------------------------
# List is Mutable
# ------------------------------------------

# Mutable means we can change existing values.

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

# Output:
# ['Apple', 'Orange', 'Mango']


# ------------------------------------------
# Duplicate Values are Allowed
# ------------------------------------------

numbers = [10, 20, 10, 30, 20]

print(numbers)

# Output:
# [10, 20, 10, 30, 20]


# ------------------------------------------
# Different Data Types
# ------------------------------------------

data = ["Maruf", 26, 85.5, True]

print(data)


# ------------------------------------------
# Find Length of List
# ------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))

# Output:
# 3


# ------------------------------------------
# Check Value in List
# ------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)

# Output:
# True


print("Orange" in fruits)

# Output:
# False


# ------------------------------------------
# List Type
# ------------------------------------------

fruits = ["Apple", "Banana"]

print(type(fruits))

# Output:
# <class 'list'>


# ==========================================
# INTERVIEW QUESTIONS
# ==========================================

# Q1. What is a list in Python?
#
# Answer:
# A list is an ordered and mutable collection
# used to store multiple values.


# Q2. Is a list mutable or immutable?
#
# Answer:
# A list is mutable.
# We can change, add and remove its elements.


# Q3. Does a list allow duplicate values?
#
# Answer:
# Yes, lists allow duplicate values.


# Q4. Does list indexing start from 0?
#
# Answer:
# Yes, Python list indexing starts from 0.


# Q5. Can a list store different data types?
#
# Answer:
# Yes, a list can store different data types.


# Q6. How do you find the length of a list?
#
# Answer:
# We use the len() function.
#
# Example:
# len(numbers)


# Q7. How do you check whether a value
# exists in a list?
#
# Answer:
# We can use the "in" operator.
#
# Example:
# "Apple" in fruits


# ==========================================
# QUICK REVISION
# ==========================================

# List -> []
# Ordered -> Yes
# Mutable -> Yes
# Duplicates -> Allowed
# Indexing -> Starts from 0
# Negative indexing -> Supported
# Slicing -> Supported
# Different data types -> Allowed