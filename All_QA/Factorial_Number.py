# ==========================================
# FACTORIAL
# ==========================================

# Factorial ka matlab:
# Kisi number ko 1 tak ke sabhi numbers se multiply karna.
#
# Example:
# 5! = 5 × 4 × 3 × 2 × 1
#    = 120
#
# 0! = 1


# ==========================================
# 1. FACTORIAL USING FOR LOOP
# ==========================================

numEnt = int(input("Enter a number to find factorial: "))

fact = 1

# Negative number ka factorial nahi hota
if numEnt < 0:
    print("Factorial does not exist for negative numbers")

# 0 ka factorial 1 hota hai
elif numEnt == 0:
    print("The factorial of 0 is 1")

# Positive number ke liye factorial calculate karenge
else:
    for i in range(1, numEnt + 1):
        fact = fact * i

    print(f"The factorial of {numEnt} is {fact}")


# ==========================================
# 2. FACTORIAL USING RECURSION
# ==========================================

def factorial(a):

    # Base condition:
    # Jab a = 0 hoga, function yahin ruk jayega
    if a == 0:
        return 1

    # Function khud ko call kar raha hai
    # Isko recursion kehte hain
    else:
        return a * factorial(a - 1)


num = int(input("Enter a number to find factorial: "))

result = factorial(num)

print(f"The factorial of {num} is {result}")


# ==========================================
# RECURSION KO EASY SAMJHO
# ==========================================

# Agar num = 5

# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1 * factorial(0)

# factorial(0) = 1
#
# Final answer:
# 5 * 4 * 3 * 2 * 1
# = 120


# ==========================================
# INTERVIEW QUESTIONS
# ==========================================

# Q1. What is factorial?
# Answer:
# Factorial is the product of all positive integers
# from a given number down to 1.

# Q2. What is 5 factorial?
# Answer:
# 5! = 5 × 4 × 3 × 2 × 1 = 120

# Q3. What is 0 factorial?
# Answer:
# 0! = 1

# Q4. What is recursion?
# Answer:
# Recursion is when a function calls itself.

# Q5. What is a base condition?
# Answer:
# Base condition tells the recursive function when to stop.

# Q6. Why do we use fact = 1?
# Answer:
# Because we are doing multiplication,
# and 1 is the starting value for multiplication.