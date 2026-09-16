# ============================================================
# TUPLE - IMPORTANT INTERVIEW & PRACTICAL QUESTIONS
# ============================================================


# Q1. Create a Tuple and print it
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

print(numbers)

# Output:
# (10, 20, 30, 40)


# Q2. Print the first element of a Tuple
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

print(numbers[0])

# Output:
# 10


# Q3. Print the last element
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

print(numbers[-1])

# Output:
# 40


# Q4. Find the length of a Tuple
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

print(len(numbers))

# Output:
# 4


# Q5. Check if a value exists in Tuple
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

if 20 in numbers:
    print("20 is present")

# Output:
# 20 is present


# Q6. Count how many times a value appears
# ------------------------------------------------------------

numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))

# Output:
# 3


# Q7. Find the index of a value
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

print(numbers.index(30))

# Output:
# 2


# Q8. Find the largest value
# ------------------------------------------------------------

numbers = (10, 50, 20, 80, 30)

print(max(numbers))

# Output:
# 80


# Q9. Find the smallest value
# ------------------------------------------------------------

numbers = (10, 50, 20, 80, 30)

print(min(numbers))

# Output:
# 10


# Q10. Find the sum of Tuple values
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

print(sum(numbers))

# Output:
# 100


# Q11. Reverse a Tuple
# ------------------------------------------------------------

numbers = (10, 20, 30, 40)

reversed_tuple = numbers[::-1]

print(reversed_tuple)

# Output:
# (40, 30, 20, 10)


# Q12. Convert List into Tuple
# ------------------------------------------------------------

numbers = [10, 20, 30]

numbers = tuple(numbers)

print(numbers)

# Output:
# (10, 20, 30)


# Q13. Convert Tuple into List
# ------------------------------------------------------------

numbers = (10, 20, 30)

numbers = list(numbers)

print(numbers)

# Output:
# [10, 20, 30]


# Q14. Loop through a Tuple
# ------------------------------------------------------------

numbers = (10, 20, 30)

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30


# Q15. Find duplicate values
# ------------------------------------------------------------

numbers = (10, 20, 20, 30, 30, 40)

for num in numbers:
    if numbers.count(num) > 1:
        print(num)

# Output:
# 20
# 20
# 30
# 30
#
# NOTE:
# This prints duplicate values more than once.
# We will learn a better method using Set.


# ============================================================
# IMPORTANT THEORY QUESTIONS
# ============================================================


# Q16. Is Tuple mutable or immutable?
#
# Answer:
# Tuple is immutable.
#
# It means we cannot change its values after creation.


# Q17. Does Tuple allow duplicate values?

# Answer:
# Yes, Tuple allows duplicate values.


# Q18. Can Tuple store different data types?

# Answer:
# Yes.

# Example:
# data = ("Maruf", 26, True)


# Q19. What is the main difference between List and Tuple?

# Answer:
# List is mutable.
# Tuple is immutable.


# Q20. How many important built-in methods does Tuple have?

# Mainly two:

# count()
# index()


# ============================================================
# EASY MEMORY
# ============================================================

# uple = Ordered + Immutable

# count() -> How many?
# index() -> Which position?
# len()   -> How many total values?
# max()   -> Largest
# min()   -> Smallest
# sum()   -> Total

# List  -> []
# Tuple -> ()

# ============================================================