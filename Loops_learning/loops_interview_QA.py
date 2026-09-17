# ============================================================
# LOOPS - INTERVIEW / MNC QUESTIONS
# ============================================================


# ============================================================
# Q1. What is a loop?
# ============================================================

# Answer:
# A loop is used to repeat a block of code multiple times.


# ============================================================
# Q2. What is a for loop?
# ============================================================

# Answer:
# A for loop is used to iterate over a sequence or collection.

numbers = [10, 20, 30]

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30


# ============================================================
# Q3. What is a while loop?
# ============================================================

# Answer:
# A while loop repeats code while a condition is True.

count = 1

while count <= 3:
    print(count)
    count = count + 1

# Output:
# 1
# 2
# 3


# ============================================================
# Q4. Difference between for loop and while loop?
# ============================================================

# Answer:
# for loop -> commonly used to iterate over a collection.
# while loop -> runs based on a condition.


# ============================================================
# Q5. What is break?
# ============================================================

# Answer:
# break completely stops the loop.

for num in range(1, 6):

    if num == 3:
        break

    print(num)

# Output:
# 1
# 2


# ============================================================
# Q6. What is continue?
# ============================================================

# Answer:
# continue skips the current iteration.

for num in range(1, 6):

    if num == 3:
        continue

    print(num)

# Output:
# 1
# 2
# 4
# 5


# ============================================================
# Q7. What is range()?
# ============================================================

# Answer:
# range() generates a sequence of numbers.

for num in range(1, 5):
    print(num)

# Output:
# 1
# 2
# 3
# 4


# ============================================================
# Q8. What is a nested loop?
# ============================================================

# Answer:
# A nested loop is a loop inside another loop.

for i in range(2):

    for j in range(2):
        print("Hello")

# Output:
# Hello
# Hello
# Hello
# Hello


# ============================================================
# Q9. Print even numbers from 1 to 10.
# ============================================================

for num in range(1, 11):

    if num % 2 == 0:
        print(num)

# Output:
# 2
# 4
# 6
# 8
# 10


# ============================================================
# Q10. Print odd numbers from 1 to 10.
# ============================================================

for num in range(1, 11):

    if num % 2 != 0:
        print(num)

# Output:
# 1
# 3
# 5
# 7
# 9


# ============================================================
# Q11. Find a number in a list.
# ============================================================

numbers = [10, 20, 30, 40]

for num in numbers:

    if num == 30:
        print("Found")
        break

# Output:
# Found


# ============================================================
# Q12. Print all items of a list.
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
# EASY MEMORY
# ============================================================

# for      -> collection ke items
# while    -> condition True hone tak
# range()  -> numbers ki sequence
# break    -> STOP the loop
# continue -> SKIP current iteration
# nested   -> loop ke andar loop


# ============================================================
# IMPORTANT
# ============================================================

# while loop me condition ko eventually False banana zaroori hai.
#
# Example:
#
# count = 1
#
# while count <= 5:
#     print(count)
#     count = count + 1
#
# Agar count update nahi karenge,
# to infinite loop ho sakta hai.


# ============================================================
# LOOPS COMPLETED ✅
# ============================================================