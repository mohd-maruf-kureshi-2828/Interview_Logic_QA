# ============================================================
# PYTHON TUPLE - INTERVIEW NOTES
# ============================================================


# 1. WHAT IS A TUPLE?
# ------------------------------------------------------------
# A Tuple is used to store multiple values in one variable.
#
# Tuple is:
# 1. Ordered
# 2. Immutable
# 3. Allows duplicate values
# 4. Can store different data types

# Immutable means:
# We cannot change, add, or remove values from a Tuple.


# 2. TUPLE SYNTAX
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

print(numbers)

# Output:
# (10, 20, 30, 40)


# 3. TUPLE CAN STORE DIFFERENT DATA TYPES
# ------------------------------------------------------------

data = ("Maruf", 26, True)

print(data)

# Output:
# ('Maruf', 26, True)


# 4. TUPLE INDEXING
# ------------------------------------------------------------
# Index starts from 0.

numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[2])

# Output:
# 10
# 30


# Index:
# 10 -> index 0
# 20 -> index 1
# 30 -> index 2
# 40 -> index 3


# 5. NEGATIVE INDEXING
# ------------------------------------------------------------
# -1 means last value.

numbers = (10, 20, 30, 40)

print(numbers[-1])
print(numbers[-2])

# Output:
# 40
# 30


# 6. TUPLE SLICING
# ------------------------------------------------------------
# Slicing is similar to List.

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

# Output:
# (20, 30, 40)


# 7. TUPLE IS IMMUTABLE
# ------------------------------------------------------------
# We cannot change a Tuple value.

numbers = (10, 20, 30)

# numbers[0] = 100

# This will give an error.
# TypeError: 'tuple' object does not support item assignment


# IMPORTANT:
# List  -> Mutable   -> Can change
# Tuple -> Immutable -> Cannot change


# 8. DUPLICATE VALUES
# ------------------------------------------------------------
# Tuple allows duplicate values.

numbers = (10, 20, 20, 30)

print(numbers)

# Output:
# (10, 20, 20, 30)


# 9. len() WITH TUPLE
# ------------------------------------------------------------
# len() tells us how many values are present.

numbers = (10, 20, 30, 40)

print(len(numbers))

# Output:
# 4


# 10. 'in' OPERATOR
# ------------------------------------------------------------
# 'in' checks whether a value exists in the Tuple.

numbers = (10, 20, 30, 40)

print(20 in numbers)
print(50 in numbers)

# Output:
# True
# False


# 11. count()
# ------------------------------------------------------------
# count() tells how many times a value appears.

numbers = (10, 20, 20, 30)

print(numbers.count(20))

# Output:
# 2


# 12. index()
# ------------------------------------------------------------
# index() tells the position of a value.

numbers = (10, 20, 30, 40)

print(numbers.index(30))

# Output:
# 2


# 13. LOOP THROUGH A TUPLE
# ------------------------------------------------------------

numbers = (10, 20, 30)

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30


# 14. TUPLE VS LIST
# ------------------------------------------------------------

# List:
# numbers = [10, 20, 30]

# Tuple:
# numbers = (10, 20, 30)

# List is Mutable.
# Tuple is Immutable.

# List uses []
# Tuple uses ()

# Both are:
# - Ordered
# - Allow duplicates
# - Support indexing
# - Support slicing


# 15. WHY USE TUPLE?
# ------------------------------------------------------------
# We use Tuple when data should not be changed.

# Example:

# days = ("Monday", "Tuesday", "Wednesday")

# These values are fixed, so Tuple can be useful.


# 16. IMPORTANT INTERVIEW QUESTION
# ------------------------------------------------------------
# Q: What is a Tuple?

# Answer:
# "A Tuple is an ordered and immutable collection
# used to store multiple values."


# 17. IMPORTANT INTERVIEW QUESTION
# ------------------------------------------------------------
# Q: What is the difference between List and Tuple?

# Answer:
# "The main difference is mutability.
# A List is mutable, but a Tuple is immutable."


# 18. IMPORTANT INTERVIEW QUESTION
# ------------------------------------------------------------
# Q: Can Tuple contain duplicate values?
#
# Answer:
# "Yes, Tuple allows duplicate values."


# 19. IMPORTANT INTERVIEW QUESTION
# ------------------------------------------------------------
# Q: Can we change a Tuple?
#
# Answer:
# "No. Tuple is immutable, so we cannot change
# its values after creation."


# ============================================================
# MEMORY TRICK
# ============================================================

# List  -> [] -> Mutable
# Tuple -> () -> Immutable

# count() -> How many times?
# index() -> Which position?

# ============================================================