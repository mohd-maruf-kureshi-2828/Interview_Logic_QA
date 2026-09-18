# ==========================================
# RECURSION
# ==========================================


# THEORY:
# Recursion ek process hai jisme function
# khud ko hi call karta hai.


# ------------------------------------------
# 1. SIMPLE RECURSION EXAMPLE
# ------------------------------------------

def countdown(n):

    # Base condition
    # Ye recursion ko stop karti hai

    if n == 0:
        return

    print(n)

    # Function khud ko call kar raha hai

    countdown(n - 1)


countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1


# ------------------------------------------
# 2. BASE CONDITION
# ------------------------------------------

# Base condition wo condition hai
# jaha recursion stop hoti hai.

# Example:

# if n == 0:
#     return


# ------------------------------------------
# 3. RECURSIVE CALL
# ------------------------------------------

# Jab function khud ko call karta hai,
# usko recursive call kehte hain.

# Example:

# countdown(n - 1)


# ------------------------------------------
# 4. FACTORIAL USING RECURSION
# ------------------------------------------

def factorial(n):

    # Base condition

    if n == 0:
        return 1

    # Recursive call

    return n * factorial(n - 1)


print(factorial(5))

# Output:
# 120


# ==========================================
# IMPORTANT POINTS
# ==========================================

# Recursion = function calls itself
#
# Base condition = recursion ko stop karti hai
#
# Recursive call = function ka khud ko call karna
#
# Base condition nahi hogi to recursion
# continuously chal sakti hai.


# ==========================================
# INTERVIEW QUESTIONS & ANSWERS
# ==========================================


# Q1. What is recursion?
#
# Answer:
# Recursion is a process where a function
# calls itself.


# Q2. What is a base condition?
#
# Answer:
# A base condition is the condition that
# stops the recursion.


# Q3. Why is a base condition important?
#
# Answer:
# It stops the recursive calls and prevents
# the function from running continuously.


# Q4. What is a recursive call?
#
# Answer:
# When a function calls itself,
# it is called a recursive call.


# Q5. Give an example of recursion.
#
# Answer:
# Factorial is a common example of recursion.


# Q6. What happens if recursion does not
# have a proper base condition?
#
# Answer:
# Python can raise a RecursionError.


# Q7. Can we solve factorial using recursion?
#
# Answer:
# Yes.


# ==========================================
# EASY MEMORY
# ==========================================

# Recursion -> Function calls itself
# Base condition -> Stops recursion
# Recursive call -> Function calls itself