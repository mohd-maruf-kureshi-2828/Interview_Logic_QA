# ============================================================
# WHILE LOOP
# ============================================================

# Theory:
# while loop ek kaam ko baar-baar repeat karta hai
# jab tak given condition True hoti hai.
#
# Basic syntax:
#
# while condition:
#     kaam


# ------------------------------------------------------------
# Example 1: Print 1 to 5
# ------------------------------------------------------------

count = 1

while count <= 5:
    print(count)
    count = count + 1

# Output:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------------------------
# How it works:
# ------------------------------------------------------------

# count = 1
# Check: 1 <= 5 -> True -> print 1
# count becomes 2
#
# Check: 2 <= 5 -> True -> print 2
# count becomes 3
#
# Check: 3 <= 5 -> True -> print 3
# count becomes 4
#
# Check: 4 <= 5 -> True -> print 4
# count becomes 5
#
# Check: 5 <= 5 -> True -> print 5
# count becomes 6
#
# Check: 6 <= 5 -> False
# Loop stops.


# ------------------------------------------------------------
# Example 2: Print 5 to 1
# ------------------------------------------------------------

count = 5

while count >= 1:
    print(count)
    count = count - 1

# Output:
# 5
# 4
# 3
# 2
# 1


# ------------------------------------------------------------
# Example 3: Loop through a list using while
# ------------------------------------------------------------

numbers = [10, 20, 30, 40]

index = 0

while index < len(numbers):
    print(numbers[index])
    index = index + 1

# Output:
# 10
# 20
# 30
# 40


# ------------------------------------------------------------
# Example 4: User input
# ------------------------------------------------------------

# number = int(input("Enter a number: "))
#
# while number <= 5:
#     print(number)
#     number = number + 1


# ------------------------------------------------------------
# FOR LOOP vs WHILE LOOP
# ------------------------------------------------------------

# for loop:
# Jab hume collection ke items par loop chalana ho
# ya fixed number of times repeat karna ho.
#
# Example:
#
# for num in [10, 20, 30]:
#     print(num)


# while loop:
# Jab loop condition ke basis par chalana ho.
#
# Example:
#
# count = 1
#
# while count <= 5:
#     print(count)
#     count = count + 1


# ------------------------------------------------------------
# INTERVIEW QUESTIONS
# ------------------------------------------------------------

# Q1. What is a while loop?
#
# Answer:
# A while loop repeats a block of code
# while a given condition is True.


# Q2. Why do we update the variable in a while loop?
#
# Answer:
# We update the variable so that the condition
# can eventually become False and the loop can stop.


# Q3. What happens if the condition never becomes False?
#
# Answer:
# The loop can become an infinite loop.


# Q4. Difference between for and while loop?
#
# Answer:
# A for loop is commonly used to iterate over a collection
# or a known sequence of values.
#
# A while loop runs based on a condition.


# ------------------------------------------------------------
# EASY MEMORY TRICK
# ------------------------------------------------------------

# for:
# "Collection ke items par chalo"
#
# while:
# "Condition True hai tab tak chalo"


# Golden Template:
#
# variable = starting_value
#
# while condition:
#     kaam
#     variable = update