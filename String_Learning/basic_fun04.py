# ==========================================
# STRING METHODS - find(), index(), count()
# ==========================================


# ------------------------------------------
# 1. find()
# ------------------------------------------

# find() searches for a character or text
# inside a string.

# It returns the index (position) where
# the text is found.

text = "Python"

result = text.find("t")

print(result)

# Output:
# 2


# Remember:
# P = 0
# y = 1
# t = 2
# h = 3
# o = 4
# n = 5


# If the text is not found,
# find() returns -1.

text = "Python"

print(text.find("z"))

# Output:
# -1


# find() can search for a complete word too.

text = "I love Python"

print(text.find("Python"))

# Output:
# 7


# ------------------------------------------
# 2. index()
# ------------------------------------------

# index() also searches for text
# and returns its position.

text = "Python"

print(text.index("t"))

# Output:
# 2


# Main difference between find() and index():
#
# find() -> returns -1 if not found
# index() -> gives an error if not found


text = "Python"

print(text.find("z"))

# Output:
# -1


# This will give ValueError:
# print(text.index("z"))


# ------------------------------------------
# 3. count()
# ------------------------------------------

# count() counts how many times
# a character or text appears.

text = "banana"

print(text.count("a"))

# Output:
# 3


text = "banana"

print(text.count("n"))

# Output:
# 2


# count() can also count a complete word.

text = "I love Python and Python is easy"

print(text.count("Python"))

# Output:
# 2


# If the text is not present,
# count() returns 0.

text = "Python"

print(text.count("Java"))

# Output:
# 0


# ==========================================
# INTERVIEW QUESTIONS
# ==========================================

# Q1. What does find() do?

# Answer:
# find() searches for a substring and returns
# its index. If it is not found, it returns -1.


# Q2. What does index() do?

# Answer:
# index() searches for a substring and returns
# its index. If it is not found, it raises ValueError.


# Q3. Difference between find() and index()?

# Answer:
# find() returns -1 when the value is not found.
# index() raises ValueError when the value is not found.


# Q4. What does count() do?

# Answer:
# count() returns the number of times a
# character or substring appears in a string.


# ==========================================
# QUICK REVISION
# ==========================================

# find()  -> position, not found = -1
# index() -> position, not found = ValueError
# count() -> number of occurrences