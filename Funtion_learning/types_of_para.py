# ============================================================
# FUNCTION PARAMETERS - COMPLETE BASICS
# ============================================================


# ============================================================
# Parameter and Argument
# ============================================================

# Parameter:
# Function banate waqt () ke andar jo variable hota hai.

def greet(name):
    print("Hello", name)


# name = parameter


# Argument:
# Function call karte waqt jo actual value dete hain.

greet("Maruf")

# "Maruf" = argument


# Easy memory:
# Parameter -> function banate time
# Argument  -> function call karte time


# ============================================================
# 1. POSITIONAL ARGUMENT
# ============================================================

# Position/order important hota hai.

def student(name, age):
    print(name)
    print(age)


student("Maruf", 26)

# Output:
# Maruf
# 26


# name = "Maruf"
# age = 26


# ============================================================
# 2. KEYWORD ARGUMENT
# ============================================================

# Parameter ka naam likhkar value dete hain.

def student_info(name, age):
    print(name)
    print(age)


student_info(age=26, name="Maruf")

# Output:
# Maruf
# 26


# Order change kar sakte hain
# because parameter names are given.


# ============================================================
# 3. DEFAULT PARAMETER
# ============================================================

# Parameter ko default value de sakte hain.

def welcome(name="Guest"):
    print("Hello", name)


welcome()

# Output:
# Hello Guest


welcome("Maruf")

# Output:
# Hello Maruf


# Value nahi di -> Guest
# Value di -> given value


# ============================================================
# 4. *args
# ============================================================

# *args multiple positional arguments accept karta hai.

def numbers(*args):
    print(args)


numbers(10, 20, 30, 40)

# Output:
# (10, 20, 30, 40)


# *args -> tuple


# ============================================================
# 5. **kwargs
# ============================================================

# **kwargs multiple keyword arguments accept karta hai.

def student_data(**kwargs):
    print(kwargs)


student_data(name="Maruf", age=26)

# Output:
# {'name': 'Maruf', 'age': 26}


# **kwargs -> dictionary


# ============================================================
# 6. REQUIRED PARAMETER
# ============================================================

# Required parameter ki value dena zaroori hai.

def hello(name):
    print("Hello", name)


hello("Maruf")

# Output:
# Hello Maruf


# hello() nahi kar sakte
# because name ki value required hai.


# ============================================================
# 7. POSITIONAL + KEYWORD
# ============================================================

def person(name, age):
    print(name)
    print(age)


person("Maruf", age=26)

# Output:
# Maruf
# 26


# "Maruf" -> positional argument
# age=26  -> keyword argument


# ============================================================
# IMPORTANT RULE
# ============================================================

# Positional argument ko keyword argument ke
# baad nahi likh sakte.


# Wrong:

# person(age=26, "Maruf")


# Correct:

# person("Maruf", age=26)


# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

# Q1. What is a parameter?

# Answer:
# A parameter is a variable defined in a function.


# Q2. What is an argument?

# Answer:
# An argument is the actual value passed to a function.


# Q3. What is a positional argument?

# Answer:
# A positional argument is assigned based on its position.


# Q4. What is a keyword argument?

# Answer:
# A keyword argument is passed using the parameter name.


# Q5. What is a default parameter?

# Answer:
# A default parameter has a default value.


# Q6. What is *args?

# Answer:
# *args allows multiple positional arguments.
# It stores them as a tuple.


# Q7. What is **kwargs?

# Answer:
# **kwargs allows multiple keyword arguments.
# It stores them as a dictionary.


# ============================================================
# FINAL MEMORY
# ============================================================

# Positional -> ORDER

# Keyword -> NAME

# Default -> DEFAULT VALUE

# *args -> MANY VALUES -> TUPLE

# **kwargs -> MANY KEY=VALUE -> DICTIONARY

# Required -> VALUE IS COMPULSORY
