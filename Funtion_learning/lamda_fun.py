# ==========================================
# LAMBDA FUNCTION
# ==========================================


# THEORY:
# Lambda ek small one-line function hota hai.
# Lambda function ko anonymous function bhi bolte hain.
# Isme normally def keyword use nahi hota.


# ------------------------------------------
# 1. SIMPLE LAMBDA
# ------------------------------------------

greet = lambda name: "Hello " + name

print(greet("Maruf"))

# Output:
# Hello Maruf


# ------------------------------------------
# 2. LAMBDA WITH TWO PARAMETERS
# ------------------------------------------

add = lambda a, b: a + b

print(add(10, 20))

# Output:
# 30


# ------------------------------------------
# 3. LAMBDA VS NORMAL FUNCTION
# ------------------------------------------

# Normal function:

def square(number):
    return number * number

print(square(5))

# Output:
# 25


# Lambda:

square = lambda number: number * number

print(square(5))

# Output:
# 25


# ------------------------------------------
# IMPORTANT POINTS
# ------------------------------------------

# Lambda is generally used for:
# - Small functions
# - One-line operations
# - Simple logic


# Lambda syntax:
#
# lambda parameters: expression
#
# Example:
#
# lambda name: "Hello " + name


# ==========================================
# INTERVIEW QUESTIONS & ANSWERS
# ==========================================


# Q1. What is a lambda function?
#
# Answer:
# Lambda is a small anonymous function
# written in one line.


# Q2. Which keyword is used to create
# a lambda function?
#
# Answer:
# lambda


# Q3. Can a lambda function have
# multiple parameters?
#
# Answer:
# Yes, lambda can have multiple parameters.
#
# Example:
#
# add = lambda a, b: a + b


# Q4. What is the difference between
# normal function and lambda function?
#
# Answer:
# Normal function is created using def,
# while lambda is used for small
# one-line functions.


# Q5. Does lambda return a value?
#
# Answer:
# Yes, the expression in a lambda
# automatically returns its result.


# Q6. What is the syntax of lambda?
#
# Answer:
# lambda parameters: expression


# ==========================================
# EASY MEMORY
# ==========================================

# lambda = small one-line function
# def    = normal function