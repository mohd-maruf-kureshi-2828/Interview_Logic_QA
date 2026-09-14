# ==========================================
# PYTHON LIST METHODS
# ==========================================


# ------------------------------------------
# 1. append()
# ------------------------------------------

# append() adds ONE element at the end of a list.

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']


# Real-world:
# New item/user/product ko list me add karna.


# ------------------------------------------
# 2. extend()
# ------------------------------------------

# extend() adds MULTIPLE elements
# from another iterable to the list.

fruits = ["Apple", "Banana"]

fruits.extend(["Mango", "Orange"])

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango', 'Orange']


# append() vs extend()

fruits = ["Apple", "Banana"]

fruits.append(["Mango", "Orange"])

print(fruits)

# Output:
# ['Apple', 'Banana', ['Mango', 'Orange']]


fruits = ["Apple", "Banana"]

fruits.extend(["Mango", "Orange"])

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango', 'Orange']


# Easy memory:
# append()  -> one item
# extend()  -> multiple items


# ------------------------------------------
# 3. insert()
# ------------------------------------------

# insert() adds an element at a specific index.

fruits = ["Apple", "Mango"]

fruits.insert(1, "Banana")

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']


# Syntax:
# list.insert(index, value)


# ------------------------------------------
# 4. remove()
# ------------------------------------------

# remove() removes the first matching value.

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

# Output:
# ['Apple', 'Mango']


# ------------------------------------------
# 5. pop()
# ------------------------------------------

# pop() removes an element using its index
# and returns the removed value.

fruits = ["Apple", "Banana", "Mango"]

removed = fruits.pop(1)

print(removed)
print(fruits)

# Output:
# Banana
# ['Apple', 'Mango']


# If index is not given,
# pop() removes the last element.

fruits = ["Apple", "Banana", "Mango"]

removed = fruits.pop()

print(removed)
print(fruits)

# Output:
# Mango
# ['Apple', 'Banana']


# Easy memory:
# remove() -> remove by VALUE
# pop()    -> remove by INDEX


# ------------------------------------------
# 6. clear()
# ------------------------------------------

# clear() removes all elements from a list.

fruits = ["Apple", "Banana", "Mango"]

fruits.clear()

print(fruits)

# Output:
# []


# ------------------------------------------
# 7. index()
# ------------------------------------------

# index() returns the position of
# the first matching value.

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))

# Output:
# 1


# ------------------------------------------
# 8. count()
# ------------------------------------------

# count() tells how many times
# a value appears in the list.

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

# Output:
# 3


# ------------------------------------------
# 9. sort()
# ------------------------------------------

# sort() arranges list elements
# in ascending order by default.

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# Output:
# [10, 20, 30, 40]


# Descending order:

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# Output:
# [40, 30, 20, 10]


# ------------------------------------------
# 10. reverse()
# ------------------------------------------

# reverse() reverses the order
# of elements in the existing list.

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

# Output:
# [40, 30, 20, 10]


# ==========================================
# INTERVIEW QUESTIONS
# ==========================================

# Q1. Difference between append() and extend()?
#
# Answer:
# append() adds one element to the list.
# extend() adds multiple elements from an iterable.


# Q2. Difference between remove() and pop()?
#
# Answer:
# remove() removes an element by value.
# pop() removes an element by index
# and returns the removed element.


# Q3. What does insert() do?
#
# Answer:
# insert() adds an element at a specified index.


# Q4. What does clear() do?
#
# Answer:
# clear() removes all elements from the list.


# Q5. What does count() do?
#
# Answer:
# count() returns the number of times
# a value appears in a list.


# Q6. What does index() do?
#
# Answer:
# index() returns the index of the first
# matching element.


# Q7. What does sort() do?
#
# Answer:
# sort() sorts the list in ascending order
# by default.


# Q8. What does reverse() do?
#
# Answer:
# reverse() reverses the order of elements
# in the list.


# ==========================================
# QUICK REVISION
# ==========================================

# append()  -> add one element
# extend()  -> add multiple elements
# insert()  -> add at specific position
# remove()  -> remove by value
# pop()     -> remove by index
# clear()   -> remove everything
# index()   -> find position
# count()   -> count occurrences
# sort()    -> arrange elements
# reverse() -> reverse order