# ==========================================
# RAISE KEYWORD
# ==========================================


# THEORY:
# raise ka use hum manually exception
# generate karne ke liye karte hain.


# ------------------------------------------
# 1. SIMPLE RAISE
# ------------------------------------------

age = 15

if age < 18:
    raise Exception("Age must be 18 or above")

# Output:
# Exception: Age must be 18 or above


# ------------------------------------------
# 2. RAISE WITH VALUEERROR
# ------------------------------------------

age = 15

if age < 18:
    raise ValueError("You must be 18 or above")

# Output:
# ValueError: You must be 18 or above


# ------------------------------------------
# 3. RAISE + TRY + EXCEPT
# ------------------------------------------

try:
    age = 15

    if age < 18:
        raise ValueError("Age is not valid")

except ValueError as error:
    print(error)

# Output:
# Age is not valid


# ==========================================
# EASY MEMORY
# ==========================================

# raise = manually error create karna


# ==========================================
# INTERVIEW QUESTIONS & ANSWERS
# ==========================================


# Q1. What is raise in Python?
#
# Answer:
# raise is used to manually raise an exception.


# Q2. Why do we use raise?
#
# Answer:
# We use raise when we want to create
# an exception based on our own condition.


# Q3. Can raise be used with try and except?
#
# Answer:
# Yes.


# Q4. Give a real-world example of raise.
#
# Answer:
# We can use raise to validate user input,
# such as checking age, password or amount.


# Q5. What is the difference between
# raise and except?
#
# Answer:
# raise creates or generates an exception,
# while except handles an exception.