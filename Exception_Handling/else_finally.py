# ==========================================
# ELSE AND FINALLY
# ==========================================


# ==========================================
# 1. ELSE
# ==========================================

# THEORY:
# else block tab execute hota hai
# jab try block me koi error nahi aata.


try:
    num = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division successful")

# Output:
# Division successful


# ------------------------------------------
# 2. TRY ME ERROR AAYE TO ELSE NAHI CHALEGA
# ------------------------------------------

try:
    num = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division successful")

# Output:
# Cannot divide by zero


# ==========================================
# 3. FINALLY
# ==========================================

# THEORY:
# finally block normally hamesha execute hota hai.
# Error aaye ya na aaye, finally run hota hai.


try:
    num = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")

# Output:
# Program finished


# ------------------------------------------
# 4. TRY + EXCEPT + ELSE + FINALLY
# ------------------------------------------

try:
    num = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division successful")

finally:
    print("Program finished")

# Output:
# Division successful
# Program finished


# ==========================================
# EASY MEMORY
# ==========================================

# try     = risky code
# except  = error handle
# else    = error nahi aaya to chalega
# finally = normally hamesha chalega


# ==========================================
# INTERVIEW QUESTIONS & ANSWERS
# ==========================================


# Q1. What is else in exception handling?
#
# Answer:
# else runs when no exception occurs
# in the try block.


# Q2. When does else block execute?
#
# Answer:
# It executes when the try block
# runs successfully without an error.


# Q3. What is finally?
#
# Answer:
# finally is a block that normally executes
# whether an exception occurs or not.


# Q4. Is finally always executed?
#
# Answer:
# Normally yes, finally executes whether
# an exception occurs or not.


# Q5. Can we use else and finally together?
#
# Answer:
# Yes.


# Q6. What is the order of execution?
#
# Answer:
# try -> except/else -> finally


# ==========================================
# QUICK REVISION
# ==========================================

# try:
#     risky code
#
# except:
#     error handling
#
# else:
#     no error
#
# finally:
#     cleanup / final code