# ==========================================
# STRING METHODS - split() and join()
# ==========================================


# ------------------------------------------
# 1. split()
# ------------------------------------------

# split() breaks a string into multiple parts
# and returns a LIST.

text = "Python is easy"

result = text.split()

print(result)

# Output:
# ['Python', 'is', 'easy']


# By default, split() uses spaces as separator.

text = "I am learning Python"

print(text.split())

# Output:
# ['I', 'am', 'learning', 'Python']


# We can give our own separator.

text = "apple,banana,mango"

result = text.split(",")

print(result)

# Output:
# ['apple', 'banana', 'mango']


# Here "," is the separator.
# split(",") means:
# Break the string wherever "," is found.


# Example with hyphen:

date = "14-09-2026"

print(date.split("-"))

# Output:
# ['14', '09', '2026']


# Important:
# split() returns a LIST.

text = "Hello World"

result = text.split()

print(type(result))

# Output:
# <class 'list'>


# ------------------------------------------
# 2. join()
# ------------------------------------------

# join() does the opposite of split().
# It joins multiple strings together.
# join() works with an iterable like a list.


words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)

# Output:
# Python is easy


# Here:
# " " means we want a space between words.
#
# join(words) joins all items of the list.


# Join using comma:

fruits = ["Apple", "Banana", "Mango"]

result = ",".join(fruits)

print(result)

# Output:
# Apple,Banana,Mango


# Join using hyphen:

numbers = ["14", "09", "2026"]

result = "-".join(numbers)

print(result)

# Output:
# 14-09-2026


# ------------------------------------------
# split() vs join()
# ------------------------------------------

# split()
# String -> List

text = "Python is easy"

words = text.split()

print(words)

# Output:
# ['Python', 'is', 'easy']


# join()
# List -> String

words = ["Python", "is", "easy"]

text = " ".join(words)

print(text)

# Output:
# Python is easy


# ------------------------------------------
# Very Important Example
# ------------------------------------------

# We can use split() and join() together.

text = "Python is very easy"

words = text.split()

result = "-".join(words)

print(result)

# Output:
# Python-is-very-easy


# First:
# split() converted string into list.

# ['Python', 'is', 'very', 'easy']

# Then:
# join() converted the list back into a string.

# Python-is-very-easy


# ==========================================
# INTERVIEW QUESTIONS
# ==========================================

# Q1. What does split() do?

# Answer:
# split() breaks a string into multiple parts
# and returns them as a list.


# Q2. What does split() return?

# Answer:
# split() returns a list.


# Q3. What is the default separator of split()?

# Answer:
# By default, split() uses whitespace as the separator.


# Q4. What does join() do?

# Answer:
# join() joins multiple strings into a single string.


# Q5. What is the difference between split()
# and join()?

# Answer:
# split() converts a string into a list.
# join() converts multiple strings, usually from
# a list, into one string.


# Q6. Give an example of split().

# Answer:
# text = "Hello World"
# text.split()

# Output:
# ['Hello', 'World']


# Q7. Give an example of join().

# Answer:
# words = ["Hello", "World"]
# " ".join(words)

# Output:
# Hello World