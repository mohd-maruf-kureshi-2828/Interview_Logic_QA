# ==========================================
# STRING METHODS - upper() and lower()
# ==========================================


# upper()
# upper() converts all letters of a string into uppercase.

name = "maruf"

print(name.upper())

# Output:
# MARUF


# lower()
# lower() converts all letters of a string into lowercase.

name = "MARUF"

print(name.lower())

# Output:
# maruf


# Original string does not change.
# Strings are immutable.

name = "Maruf"

print(name.upper())
print(name)

# Output:
# MARUF
# Maruf


# ==========================================
# INTERVIEW QUESTIONS
# ==========================================

# Q1. What does upper() do?
#
# Answer:
# upper() converts all alphabetic characters
# of a string into uppercase.


# Q2. What does lower() do?
#
# Answer:
# lower() converts all alphabetic characters
# of a string into lowercase.


# Q3. Do upper() and lower() change the original string?
#
# Answer:
# No. Strings are immutable in Python.
# These methods return a new string.


# Example:

text = "Hello"

new_text = text.upper()

print(text)
print(new_text)

# Output:
# Hello
# HELLO