# ============================================================
# PYTHON LIST & DICTIONARY COMPREHENSION - BASIC NOTES
# ============================================================

# Comprehension ka use short way me
# list ya dictionary create karne ke liye hota hai.


# ============================================================
# 1. NORMAL WAY - LIST
# ============================================================

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# ============================================================
# 2. LIST COMPREHENSION
# ============================================================

numbers = [i for i in range(1, 6)]

print(numbers)

# Same result:
# [1, 2, 3, 4, 5]


# Basic syntax:
#
# [expression for item in sequence]


# ============================================================
# 3. SQUARE NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 4. LIST COMPREHENSION WITH CONDITION
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

# Output:
# [2, 4, 6]


# Easy meaning:
#
# x for x in numbers
#       ↓
# Take each x from numbers
#
# if x % 2 == 0
#       ↓
# Keep only even numbers


# ============================================================
# 5. ODD NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = [x for x in numbers if x % 2 != 0]

print(odd_numbers)

# Output:
# [1, 3, 5]


# ============================================================
# 6. STRING LIST
# ============================================================

names = ["maruf", "rahul", "aman"]

upper_names = [name.upper() for name in names]

print(upper_names)

# Output:
# ['MARUF', 'RAHUL', 'AMAN']


# ============================================================
# 7. IF-ELSE IN LIST COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ============================================================
# 8. DICTIONARY COMPREHENSION
# ============================================================

# Dictionary comprehension ka use
# dictionary ko short way me create karne ke liye hota hai.


numbers = [1, 2, 3, 4, 5]

squares = {x: x * x for x in numbers}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Basic syntax:
#
# {key: value for item in sequence}


# ============================================================
# 9. DICTIONARY WITH CONDITION
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    x: x * x
    for x in numbers
    if x % 2 == 0
}

print(even_squares)

# Output:
# {2: 4, 4: 16, 6: 36}


# ============================================================
# 10. MOST IMPORTANT MEMORY
# ============================================================

# List comprehension:
#
# [expression for item in sequence]
#
# Example:
#
# [x * 2 for x in numbers]


# Dictionary comprehension:
#
# {key: value for item in sequence}
#
# Example:
#
# {x: x * x for x in numbers}


# ============================================================
# 11. WHEN TO USE?
# ============================================================

# Comprehension is useful when:
#
# - Code is simple
# - We want to create a list quickly
# - We want to filter data
# - We want to create a dictionary quickly
#
# Don't use comprehension if the logic becomes too complex.


# ============================================================
# FINAL REVISION
# ============================================================

# List comprehension:
# Short way to create a list.
#
# Dictionary comprehension:
# Short way to create a dictionary.
#
# Main benefit:
# Less code and simple readable logic.