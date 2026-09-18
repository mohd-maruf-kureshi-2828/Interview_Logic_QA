# ==========================================
# EXCEPTION HANDLING
# ==========================================


# THEORY:
# Exception handling ka use program me
# errors ko handle karne ke liye hota hai.
#
# Main keywords:
# try
# except


# ------------------------------------------
# 1. SIMPLE EXAMPLE
# ------------------------------------------

try:
    num = 10 / 0

except:
    print("Something went wrong")

# Output:
# Something went wrong


# ------------------------------------------
# 2. HANDLING SPECIFIC ERROR
# ------------------------------------------

try:
    num = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

# Output:
# Cannot divide by zero


# ------------------------------------------
# 3. VALUE ERROR
# ------------------------------------------

try:
    num = int("hello")

except ValueError:
    print("Invalid value")

# Output:
# Invalid value


# ------------------------------------------
# HOW IT WORKS
# ------------------------------------------

# try:
#     Risky code
#
# except:
#     Error aaye to ye code chalega


# ==========================================
# INTERVIEW QUESTIONS & ANSWERS
# ==========================================


# Q1. What is exception handling?
#
# Answer:
# Exception handling is used to handle
# errors during program execution.


# Q2. Which keywords are commonly used
# for exception handling?
#
# Answer:
# try and except.
#
# Other keywords are:
# else, finally and raise.


# Q3. What is try block?
#
# Answer:
# try block contains the code that may
# cause an exception.


# Q4. What is except block?
#
# Answer:
# except block handles the exception
# when an error occurs.


# Q5. What is ZeroDivisionError?
#
# Answer:
# It occurs when we try to divide a
# number by zero.


# Example:
# 10 / 0


# Q6. What is ValueError?
#
# Answer:
# ValueError occurs when a function receives
# a value of the correct type but an
# inappropriate value.


# Example:
# int("hello")


# ==========================================
# EASY MEMORY
# ==========================================

# try    = risky code
# except = error handle