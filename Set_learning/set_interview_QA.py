# ============================================================
# PYTHON SET - BASIC + INTERVIEW NOTES
# ============================================================


# 1. WHAT IS A SET?
# ------------------------------------------------------------
# A Set is a collection used to store multiple values.
#
# Set:
# 1. Does NOT allow duplicate values
# 2. Is unordered
# 3. Is mutable
# 4. Can store different data types
#
# Simple memory:
# Set = Unique values


# 2. SET SYNTAX
# ------------------------------------------------------------

numbers = {10, 20, 30, 40}

print(numbers)

# Output:
# {10, 20, 30, 40}


# 3. DUPLICATE VALUES
# ------------------------------------------------------------
# Set automatically removes duplicate values.

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)

# Output:
# {10, 20, 30, 40}


# IMPORTANT:
# Set does NOT keep duplicate values.


# 4. SET IS UNORDERED
# ------------------------------------------------------------
# Set does not use indexing like List or Tuple.
#
# So this is NOT allowed:
#
# numbers[0]
#
# Because Set has no fixed index.


# 5. ADD ONE VALUE
# ------------------------------------------------------------
# add() adds one value to a Set.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# Output:
# {10, 20, 30, 40}


# 6. ADD MULTIPLE VALUES
# ------------------------------------------------------------
# update() adds multiple values.

numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)

# Output:
# {10, 20, 30, 40, 50}


# MEMORY:
#
# add()    -> one value
# update() -> multiple values


# 7. REMOVE VALUE
# ------------------------------------------------------------
# remove() removes a specific value.

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)

# Output:
# {10, 30}


# 8. discard()
# ------------------------------------------------------------
# discard() also removes a value.
#
# Difference:
# remove() -> gives error if value does not exist
# discard() -> does not give error


numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)

# Output:
# {10, 20, 30}


# 9. clear()
# ------------------------------------------------------------
# clear() removes all values.

numbers = {10, 20, 30}

numbers.clear()

print(numbers)

# Output:
# set()


# 10. len()
# ------------------------------------------------------------

numbers = {10, 20, 30, 40}

print(len(numbers))

# Output:
# 4


# 11. CHECK VALUE USING 'in'
# ------------------------------------------------------------

numbers = {10, 20, 30}

print(20 in numbers)

# Output:
# True


# 12. LOOP THROUGH SET
# ------------------------------------------------------------

numbers = {10, 20, 30}

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30
#
# NOTE:
# Set is unordered, so the printing order can vary.


# 13. REMOVE DUPLICATES FROM A LIST
# ------------------------------------------------------------
# This is one of the most useful uses of Set.

numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)

# Output:
# [10, 20, 30, 40]
#
# NOTE:
# Converting List -> Set removes duplicates.
# Converting Set -> List gives us a List again.


# 14. COMMON VALUES BETWEEN TWO SETS
# ------------------------------------------------------------

set1 = {10, 20, 30}
set2 = {30, 40, 50}

common = set1 & set2

print(common)

# Output:
# {30}


# '&' means INTERSECTION.
# It finds values present in both Sets.


# 15. UNION
# ------------------------------------------------------------
# Union combines values from both Sets.
# Duplicate values are automatically removed.

set1 = {10, 20, 30}
set2 = {30, 40, 50}

result = set1 | set2

print(result)

# Output:
# {10, 20, 30, 40, 50}


# '|' means UNION.


# ============================================================
# IMPORTANT INTERVIEW QUESTIONS
# ============================================================


# Q1. What is a Set?
#
# Answer:
# "A Set is an unordered collection of unique values."


# Q2. Does Set allow duplicates?
#
# Answer:
# "No, Set does not allow duplicate values."


# Q3. Is Set ordered?
#
# Answer:
# "No, Set is unordered."


# Q4. Is Set mutable?
#
# Answer:
# "Yes, Set is mutable."


# Q5. Can we use indexing with Set?
#
# Answer:
# "No, Set does not support indexing."


# Q6. How do you remove duplicates from a List?
#
# Answer:
# "I can convert the List into a Set and then
# convert it back into a List."


# Example:
#
# numbers = [10, 20, 20, 30]
# numbers = list(set(numbers))


# Q7. Difference between List, Tuple and Set?
#
# List  -> Ordered + Mutable + Duplicates allowed
# Tuple -> Ordered + Immutable + Duplicates allowed
# Set   -> Unordered + Mutable + No duplicates


# ============================================================
# EASY MEMORY
# ============================================================
#
# LIST:
# []      -> duplicates allowed
#
# TUPLE:
# ()      -> duplicates allowed + cannot change
#
# SET:
# {}      -> unique values only
#
#
# add()    -> add ONE
# update() -> add MULTIPLE
# remove() -> remove value, error if missing
# discard()-> remove value, no error if missing
# clear()  -> remove everything
#
# & -> Common values
# | -> Combine values
#
# ============================================================