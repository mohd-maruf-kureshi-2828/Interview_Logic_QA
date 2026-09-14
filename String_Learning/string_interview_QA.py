# ==========================================
# PYTHON STRING - IMPORTANT INTERVIEW QUESTIONS
# ==========================================


# Q1. Reverse a String
# ------------------------------------------
# Interview:
# Reverse the given string without changing
# the original string.

text = "Python"

result = text[::-1]

print(result)

# Output:
# nohtyP


# Q2. Check if a String is Palindrome
# ------------------------------------------
# Palindrome means the string is same
# from both directions.

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Palindrome


# Q3. Count Vowels in a String
# ------------------------------------------
# Real-world use:
# Basic text analysis.

text = "Python Developer"

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(count)


# Q4. Count a Particular Character
# ------------------------------------------
# Real-world use:
# Finding how many times a character
# appears in user input or text.

text = "programming"

print(text.count("m"))

# Output:
# 2


# Q5. Remove Spaces from a String
# ------------------------------------------
# Real-world use:
# Cleaning user input.

text = "Python Full Stack"

result = text.replace(" ", "")

print(result)

# Output:
# PythonFullStack


# Q6. Remove Extra Spaces
# ------------------------------------------
# Real-world use:
# Cleaning data received from users.

text = "   Python Developer   "

result = text.strip()

print(result)

# Output:
# Python Developer


# Q7. Convert String to Uppercase
# ------------------------------------------
# Real-world use:
# Standardizing text before comparison.

text = "python"

print(text.upper())

# Output:
# PYTHON


# Q8. Convert String to Lowercase
# ------------------------------------------

text = "PYTHON"

print(text.lower())

# Output:
# python


# Q9. Count Number of Words
# ------------------------------------------
# Real-world use:
# Text processing and validation.

text = "I am learning Python"

words = text.split()

print(len(words))

# Output:
# 4


# Q10. Check if a Word Exists in a String
# ------------------------------------------
# Real-world use:
# Searching text or validating input.

text = "I am learning Python"

if "Python" in text:
    print("Python found")
else:
    print("Python not found")

# Output:
# Python found


# Q11. Check Starting and Ending Text
# ------------------------------------------
# Real-world use:
# File extension and input validation.

filename = "resume.pdf"

if filename.endswith(".pdf"):
    print("PDF file")

if filename.startswith("resume"):
    print("Resume file")

# Output:
# PDF file
# Resume file


# Q12. Replace Text
# ------------------------------------------
# Real-world use:
# Cleaning or modifying text.

text = "I am learning Java"

result = text.replace("Java", "Python")

print(result)

# Output:
# I am learning Python


# Q13. Find Position of a Word
# ------------------------------------------
# Real-world use:
# Searching inside text.

text = "I love Python"

position = text.find("Python")

print(position)

# Output:
# 7


# Q14. Count Character Frequency
# ------------------------------------------
# Interview:
# Find how many times each character
# occurs in a string.

text = "hello"

for char in text:
    print(char, text.count(char))

# Output:
# h 1
# e 1
# l 2
# l 2
# o 1


# NOTE:
# This simple version prints repeated characters.
# Later we can make an optimized version.


# Q15. Remove Duplicate Characters
# ------------------------------------------
# Real-world use:
# Basic text/data cleaning.

text = "programming"

result = ""

for char in text:
    if char not in result:
        result += char

print(result)

# Output:
# progamin


# Q16. Check if Two Strings are Anagrams
# ------------------------------------------
# Anagram:
# Two strings containing the same characters
# with the same frequency but different order.
#
# Example:
# listen -> silent

text1 = "listen"
text2 = "silent"

if sorted(text1) == sorted(text2):
    print("Anagram")
else:
    print("Not Anagram")

# Output:
# Anagram


# Q17. Remove a Specific Character
# ------------------------------------------
# Real-world use:
# Cleaning unwanted characters from input.

text = "hello"

result = text.replace("l", "")

print(result)

# Output:
# heo


# Q18. Reverse Each Word in a String
# ------------------------------------------
# Example:
# "Hello World"
# becomes
# "olleH dlroW"

text = "Hello World"

words = text.split()

result = ""

for word in words:
    result += word[::-1] + " "

print(result.strip())

# Output:
# olleH dlroW


# Q19. Check if String Contains Only Digits
# ------------------------------------------
# Real-world use:
# Validating numbers received as text,
# such as a form input.

value = "12345"

if value.isdigit():
    print("Only digits")
else:
    print("Contains other characters")

# Output:
# Only digits


# Q20. Check if String Contains Only Alphabets
# ------------------------------------------
# Real-world use:
# Basic name/input validation.

name = "Maruf"

if name.isalpha():
    print("Only alphabets")
else:
    print("Contains other characters")

# Output:
# Only alphabets


# ==========================================
# IMPORTANT STRING METHODS FOR INTERVIEW
# ==========================================

# upper()       -> uppercase
# lower()       -> lowercase
# capitalize()  -> first character uppercase
# title()       -> first character of each word uppercase
# strip()       -> removes beginning/end spaces
# replace()     -> replaces text
# split()       -> string -> list
# join()        -> joins strings
# find()        -> finds position, returns -1 if not found
# index()       -> finds position, raises error if not found
# count()       -> counts occurrences
# startswith()  -> checks beginning
# endswith()    -> checks ending
# isdigit()     -> checks only digits
# isalpha()     -> checks only alphabets


# ==========================================
# MOST IMPORTANT FOR ENTRY-LEVEL INTERVIEW
# ==========================================

# 1. Reverse a String
# 2. Palindrome
# 3. Count Vowels
# 4. Character Frequency
# 5. Remove Duplicates
# 6. Anagram
# 7. Count Words
# 8. Check substring using "in"
# 9. Remove spaces / clean text
# 10. isdigit() / isalpha() validation