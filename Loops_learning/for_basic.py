# ============================================================
# PYTHON FOR LOOP - ZERO TO INTERVIEW
# ============================================================


# 1. WHAT IS A LOOP?
# ------------------------------------------------------------
# Loop ka use same kaam ko baar-baar karne ke liye hota hai.
#
# Example:
# Agar mujhe 5 baar "Hello" print karna hai,
# to 5 print statements likhne ki zarurat nahi.
#
# Loop automatically repeat karega.


# Without loop:

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")


# With loop:

for i in range(5):
    print("Hello")

# Output:
# Hello
# Hello
# Hello
# Hello
# Hello


# ============================================================
# 2. WHAT IS FOR LOOP?
# ============================================================
#
# for loop ka use kisi collection ke har item par
# ek-ek karke kaam karne ke liye hota hai.
#
# Collection examples:
# List
# Tuple
# String
# Set
# Dictionary
# range()


# ============================================================
# 3. SIMPLE FOR LOOP
# ============================================================

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30
# 40


# ============================================================
# 4. IS CODE ME KYA HO RAHA HAI?
# ============================================================
#
# numbers = [10, 20, 30, 40]
#
# for num in numbers:
#
# Python list se ek value uthata hai.
#
# First:
# num = 10
# print(10)
#
# Second:
# num = 20
# print(20)
#
# Third:
# num = 30
# print(30)
#
# Fourth:
# num = 40
# print(40)


# EASY LOGIC:
#
# List me se ek value lo
# ↓
# Kaam karo
# ↓
# Next value lo
# ↓
# Kaam karo
# ↓
# Jab list khatam ho jaye → loop stop


# ============================================================
# 5. FOR LOOP WITH STRING
# ============================================================
#
# String me bhi loop laga sakte hain.
# String ke characters ek-ek karke milenge.


name = "Maruf"

for char in name:
    print(char)

# Output:
# M
# a
# r
# u
# f


# Yaha:
#
# char = M
# char = a
# char = r
# char = u
# char = f


# ============================================================
# 6. FOR LOOP WITH TUPLE
# ============================================================

numbers = (10, 20, 30)

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30


# ============================================================
# 7. FOR LOOP WITH SET
# ============================================================

numbers = {10, 20, 30}

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30
#
# NOTE:
# Set unordered hai, isliye order change ho sakta hai.


# ============================================================
# 8. FOR LOOP WITH DICTIONARY
# ============================================================

person = {
    "name": "Maruf",
    "age": 26
}

for key in person:
    print(key)

# Output:
# name
# age


# Dictionary me directly loop lagane par
# keys milti hain.


# ============================================================
# 9. DICTIONARY KEY + VALUE
# ============================================================

person = {
    "name": "Maruf",
    "age": 26
}

for key, value in person.items():
    print(key, value)

# Output:
# name Maruf
# age 26


# ============================================================
# 10. range()
# ============================================================
#
# range() numbers ki sequence banata hai.
#
# range(5) means:
#
# 0, 1, 2, 3, 4
#
# 5 include nahi hota.


for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# IMPORTANT MEMORY:
#
# range(5)
# = 0 se start
# = 5 se pehle stop


# ============================================================
# 11. range(start, stop)
# ============================================================
#
# range(1, 6)
#
# means:
# 1, 2, 3, 4, 5
#
# 6 include nahi hota.


for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# 12. range(start, stop, step)
# ============================================================
#
# Step batata hai kitna jump karna hai.


for i in range(1, 11, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9


# Logic:
#
# Start = 1
# Jump = 2
# Stop before = 11


# ============================================================
# 13. PRINT SAME TEXT MULTIPLE TIMES
# ============================================================

for i in range(3):
    print("Python")

# Output:
# Python
# Python
# Python


# ============================================================
# 14. LOOP + IF
# ============================================================
#
# Loop ke andar condition bhi laga sakte hain.


numbers = [10, 15, 20, 25, 30]

for num in numbers:

    if num > 20:
        print(num)

# Output:
# 25
# 30


# Logic:
#
# 10 > 20 ❌
# 15 > 20 ❌
# 20 > 20 ❌
# 25 > 20 ✅
# 30 > 20 ✅


# ============================================================
# 15. LOOP + if/else
# ============================================================

numbers = [10, 15, 20]

for num in numbers:

    if num > 15:
        print(num, "is greater")
    else:
        print(num, "is smaller or equal")

# Output:
# 10 is smaller or equal
# 15 is smaller or equal
# 20 is greater


# ============================================================
# 16. IMPORTANT INTERVIEW QUESTION
# ============================================================
#
# Q: What is a for loop?
#
# Answer:
# "A for loop is used to iterate over items
# in a sequence or collection."


# ============================================================
# 17. IMPORTANT INTERVIEW QUESTION
# ============================================================
#
# Q: What is range()?
#
# Answer:
# "range() generates a sequence of numbers
# that can be used with loops."


# ============================================================
# 18. IMPORTANT INTERVIEW QUESTION
# ============================================================
#
# Q: Why do we use loops?
#
# Answer:
# "Loops are used to repeat a block of code
# without writing the same code multiple times."


# ============================================================
# EASY MEMORY
# ============================================================
#
# for = ek-ek karke values lene ke liye
#
# Example:
#
# numbers = [10, 20, 30]
#
# for num in numbers:
#     print(num)
#
#
# range(5)
# -> 0 1 2 3 4
#
# range(1, 6)
# -> 1 2 3 4 5
#
# range(1, 11, 2)
# -> 1 3 5 7 9
#
# ============================================================