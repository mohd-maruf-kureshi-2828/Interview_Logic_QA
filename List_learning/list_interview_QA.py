# ==========================================
# PYTHON LIST - 20 IMPORTANT INTERVIEW QUESTIONS
# ==========================================


# Q1. Find the largest element in a list
# ------------------------------------------

numbers = [10, 50, 20, 80, 30]

largest = max(numbers)

print(largest)

# Output:
# 80

# Real-world:
# Finding highest price, highest score, etc.


# Q2. Find the smallest element
# ------------------------------------------

numbers = [10, 50, 20, 80, 30]

smallest = min(numbers)

print(smallest)

# Output:
# 10


# Q3. Find the sum of all elements
# ------------------------------------------

numbers = [10, 20, 30, 40]

total = sum(numbers)

print(total)

# Output:
# 100


# Q4. Remove duplicate values
# ------------------------------------------

numbers = [10, 20, 10, 30, 20]

result = list(set(numbers))

print(result)

# Output:
# [10, 20, 30]

# Note:
# set() removes duplicates.
# Order is not guaranteed with this approach.


# Q5. Find duplicate values
# ------------------------------------------

numbers = [10, 20, 10, 30, 20, 40]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)

# Output:
# [10, 20]


# Q6. Find common elements in two lists
# ------------------------------------------

# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]

# common = []

# for num in list1:
#     if num in list2:
#         common.append(num)

# print(common)


list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = list(set(list1) & set(list2))

print(common)

# Output:
# [30, 40]


# Q7. Merge two lists
# ------------------------------------------

list1 = [10, 20]
list2 = [30, 40]

result = list1 + list2

print(result)

# Output:
# [10, 20, 30, 40]


# Q8. Reverse a list
# ------------------------------------------

numbers = [10, 20, 30, 40]

result = numbers[::-1]

print(result)

# Output:
# [40, 30, 20, 10]


# Q9. Check whether an element exists
# ------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

if "Banana" in fruits:
    print("Found")
else:
    print("Not Found")

# Output:
# Found


# Q10. Count occurrences of an element
# ------------------------------------------

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

# Output:
# 3


# Q11. Find the length of a list
# ------------------------------------------

names = ["A", "B", "C", "D"]

print(len(names))

# Output:
# 4


# Q12. Find second largest element
# ------------------------------------------

# Find Second Largest Number

numbers = [10, 50, 20, 80, 30]

# Find the largest number
largest = max(numbers)

# Remove the largest number
numbers.remove(largest)

# Find the largest number again
# This is the second largest number
second_largest = max(numbers)

print(second_largest)

# Output: 50


# Q13. Sort a list
# ------------------------------------------

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# Output:
# [10, 20, 30, 40]


# Q14. Sort a list in descending order
# ------------------------------------------

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# Output:
# [40, 30, 20, 10]


# Q15. Remove an element from a list
# ------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

# Output:
# ['Apple', 'Mango']


# Q16. Find the index of an element
# ------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Mango"))

# Output:
# 2


# Q17. Separate even and odd numbers
# ------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)

# Output:
# [2, 4, 6]
# [1, 3, 5]


# Q18. Find missing number
# ------------------------------------------

numbers = [1, 2, 3, 5]

for num in range(1, 6):
    if num not in numbers:
        print("Missing:", num)

# Output:
# Missing: 4

# Note:
# This is a common coding interview question.
# We will later learn better approaches.


# Q19. Copy a list
# ------------------------------------------

list1 = [10, 20, 30]

list2 = list1.copy()

print(list2)

# Output:
# [10, 20, 30]


# Q20. Find whether a list is empty
# ------------------------------------------

numbers = []

if not numbers:
    print("List is empty")
else:
    print("List is not empty")

# Output:
# List is empty


# ==========================================
# IMPORTANT INTERVIEW THEORY
# ==========================================

# Q1. What is a list?
#
# Answer:
# A list is an ordered and mutable collection
# used to store multiple values.


# Q2. Is a list mutable?
#
# Answer:
# Yes. We can change its elements after creation.


# Q3. Can a list contain duplicate values?
#
# Answer:
# Yes. Lists allow duplicate values.


# Q4. Can a list contain different data types?
#
# Answer:
# Yes. A list can contain different data types.


# Q5. Difference between append() and extend()?
#
# Answer:
# append() adds one element.
# extend() adds multiple elements.


# Q6. Difference between remove() and pop()?
#
# Answer:
# remove() removes by value.
# pop() removes by index and returns the removed value.


# Q7. How do you reverse a list?
#
# Answer:
# We can use reverse(), slicing [::-1],
# or other approaches depending on the requirement.


# ==========================================
# REAL-WORLD LIST USES
# ==========================================

# Lists are commonly used for:
#
# 1. Storing users
# 2. Storing products
# 3. Storing orders
# 4. Storing API data
# 5. Storing employee records
# 6. Storing search results
# 7. Storing multiple values from a database
# 8. Processing collected data