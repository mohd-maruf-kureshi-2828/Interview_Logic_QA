# ==========================================
# STRING METHODS
# strip(), replace(), capitalize(), title()
# ==========================================


# ------------------------------------------
# 1. strip()
# ------------------------------------------

# strip() removes extra spaces from the
# beginning and end of a string.

name = "   Maruf   "

print(name)
print(name.strip())

# Output:
#    Maruf
# Maruf


# Important:
# strip() middle ke spaces ko remove nahi karta.

text = "Hello   World"

print(text.strip())

# Output:
# Hello   World


# strip() can also remove specific characters
# from the beginning and end.

text = "---Hello---"

print(text.strip("-"))

# Output:
# Hello


# ------------------------------------------
# 2. replace()
# ------------------------------------------

# replace() is used to replace one
# character or text with another.

text = "I like Python"

new_text = text.replace("Python", "Django")

print(new_text)

# Output:
# I like Django


# We can replace a character too.

text = "hello"

print(text.replace("l", "x"))

# Output:
# hexxo


# We can also control how many replacements
# should happen.

text = "apple apple apple"

print(text.replace("apple", "mango", 2))

# Output:
# mango mango apple


# Important:
# replace() does not change the original string.
# It returns a new string because strings
# are immutable.


# ------------------------------------------
# 3. capitalize()
# ------------------------------------------

# capitalize() makes the first character
# uppercase and the remaining characters
# lowercase.

text = "hello WORLD"

print(text.capitalize())

# Output:
# Hello world


# ------------------------------------------
# 4. title()
# ------------------------------------------

# title() makes the first letter of
# each word uppercase.

text = "hello world"

print(text.title())

# Output:
# Hello World


text = "python full stack developer"

print(text.title())

# Output:
# Python Full Stack Developer


# ------------------------------------------
# capitalize() vs title()
# ------------------------------------------

text = "python full stack developer"

print(text.capitalize())
print(text.title())

# Output:
# Python full stack developer
# Python Full Stack Developer


# capitalize()
# Only the first character of the
# complete string becomes uppercase.


# title()
# First character of each word becomes uppercase.


# ==========================================
# INTERVIEW QUESTIONS
# ==========================================

# Q1. What does strip() do?
#
# Answer:
# strip() removes spaces or specified characters
# from the beginning and end of a string.


# Q2. Does strip() remove spaces from the middle?
#
# Answer:
# No. strip() removes spaces only from
# the beginning and end.


# Q3. What does replace() do?
#
# Answer:
# replace() replaces a specified part of
# a string with another value.


# Q4. Does replace() modify the original string?
#
# Answer:
# No. Strings are immutable, so replace()
# returns a new string.


# Q5. What does capitalize() do?
#
# Answer:
# capitalize() makes the first character
# uppercase and the remaining characters lowercase.


# Q6. What does title() do?
#
# Answer:
# title() makes the first character of
# each word uppercase.


# Q7. What is the difference between
# capitalize() and title()?
#
# Answer:
# capitalize() changes the first character
# of the complete string.
#
# title() changes the first character
# of each word to uppercase.