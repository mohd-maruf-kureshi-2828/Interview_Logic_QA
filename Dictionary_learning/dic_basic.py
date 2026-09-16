# ============================================================
# PYTHON DICTIONARY - ZERO TO INTERVIEW
# ============================================================


# 1. WHAT IS A DICTIONARY?
# ------------------------------------------------------------
# Dictionary stores data in KEY : VALUE format.
#
# Simple example:
#
# Name  -> Maruf
# Age   -> 26
# City  -> Bengaluru
#
# In Python:
#
# key   : value


student = {
    "name": "Maruf",
    "age": 26,
    "city": "Bengaluru"
}

print(student)

# Output:
# {'name': 'Maruf', 'age': 26, 'city': 'Bengaluru'}


# ============================================================
# 2. WHY DO WE USE DICTIONARY?
# ============================================================
#
# Dictionary is useful when we want to store information
# with a meaningful name (key).
#
# Example:
#
# Instead of remembering:
# 0 = name
# 1 = age
# 2 = city
#
# We can directly use:
# "name"
# "age"
# "city"
#
# This makes data easier to understand.


# ============================================================
# 3. DICTIONARY SYNTAX
# ============================================================

person = {
    "name": "Ali",
    "age": 25
}

print(person)


# ============================================================
# 4. KEY AND VALUE
# ============================================================

# In:

# "name": "Ali"

# "name" = KEY
# "Ali"  = VALUE

# Key tells us WHAT the data is.
# Value tells us WHAT the actual data is.


person = {
    "name": "Ali",
    "age": 25
}


# ============================================================
# 5. ACCESS VALUE USING KEY
# ============================================================

# IMPORTANT:
# Dictionary does not use index like List.
# We use KEY to get the value.


person = {
    "name": "Ali",
    "age": 25,
    "city": "Bengaluru"
}

print(person["name"])
print(person["age"])

# Output:
# Ali
# 25


# Simple memory:

# List:
# numbers[0]

# Dictionary:
# person["name"]


# ============================================================
# 6. ADD NEW DATA
# ============================================================

# We can add a new key and value.


person = {
    "name": "Ali",
    "age": 25
}

person["city"] = "Bengaluru"

print(person)

# Output:
# {'name': 'Ali', 'age': 25, 'city': 'Bengaluru'}


# ============================================================
# 7. CHANGE / UPDATE VALUE
# ============================================================


person = {
    "name": "Ali",
    "age": 25
}

person["age"] = 26

print(person)

# Output:
# {'name': 'Ali', 'age': 26}


# IMPORTANT:

# Same key = value gets updated.

# person["age"] = 26


# ============================================================
# 8. REMOVE DATA
# ============================================================

# del removes a key and its value.


person = {
    "name": "Ali",
    "age": 25,
    "city": "Bengaluru"
}

del person["city"]

print(person)

# Output:
# {'name': 'Ali', 'age': 25}


# ============================================================
# 9. pop()
# ============================================================

# pop() also removes a key.

# It also returns the removed value.


person = {
    "name": "Ali",
    "age": 25
}

removed = person.pop("age")

print(removed)
print(person)

# Output:
# 25
# {'name': 'Ali'}


# ============================================================
# 10. len()
# ============================================================

# len() tells how many key-value pairs are present.


person = {
    "name": "Ali",
    "age": 25,
    "city": "Bengaluru"
}

print(len(person))

# Output:
# 3


# ============================================================
# 11. CHECK IF KEY EXISTS
# ============================================================

# Use 'in'.


person = {
    "name": "Ali",
    "age": 25
}

if "name" in person:
    print("Name exists")

# Output:
# Name exists


# IMPORTANT:
# 'in' checks KEY in Dictionary.


# ============================================================
# 12. get()
# ============================================================

# get() is used to safely get a value using its key.


person = {
    "name": "Ali",
    "age": 25
}

print(person.get("name"))

# Output:
# Ali


# If key does not exist:

# person.get("city")

# It returns:
# None

# Instead of directly giving a KeyError.


# ============================================================
# 13. keys()
# ============================================================

# keys() gives all keys.


person = {
    "name": "Ali",
    "age": 25,
    "city": "Bengaluru"
}

print(person.keys())

# Output:
# dict_keys(['name', 'age', 'city'])


# ============================================================
# 14. values()
# ============================================================

# values() gives all values.


person = {
    "name": "Ali",
    "age": 25,
    "city": "Bengaluru"
}

print(person.values())

# Output:
# dict_values(['Ali', 25, 'Bengaluru'])


# ============================================================
# 15. items()
# ============================================================

# items() gives KEY + VALUE together.


person = {
    "name": "Ali",
    "age": 25
}

print(person.items())

# Output:
# dict_items([('name', 'Ali'), ('age', 25)])


# ============================================================
# 16. LOOP THROUGH DICTIONARY
# ============================================================


person = {
    "name": "Ali",
    "age": 25,
    "city": "Bengaluru"
}

for key in person:
    print(key)

# Output:
# name
# age
# city


# ============================================================
# 17. LOOP THROUGH KEY AND VALUE
# ============================================================

# This is VERY IMPORTANT for interviews.


person = {
    "name": "Ali",
    "age": 25
}

for key, value in person.items():
    print(key, value)

# Output:
# name Ali
# age 25


# Simple logic:

# key   -> name
# value -> Ali

# key   -> age
# value -> 25


# ============================================================
# 18. DUPLICATE KEYS
# ============================================================

# Dictionary does NOT keep duplicate keys.

# If the same key is written again,
# the latest value replaces the old value.


person = {
    "name": "Ali",
    "name": "Ahmed"
}

print(person)

# Output:
# {'name': 'Ahmed'}


# ============================================================
# 19. VALUES CAN BE DUPLICATE
# ============================================================

# Values can be repeated.


person = {
    "name1": "Ali",
    "name2": "Ali"
}

print(person)

# This is allowed.


# ============================================================
# 20. DICTIONARY CAN STORE DIFFERENT DATA TYPES
# ============================================================


student = {
    "name": "Maruf",
    "age": 26,
    "skills": ["Python", "Django"],
    "is_fresher": True
}

print(student)


# ============================================================
# IMPORTANT INTERVIEW QUESTIONS
# ============================================================


# Q1. What is a Dictionary?

# Answer:
# "A Dictionary is a collection that stores data
# in key-value pairs."


# Q2. How do you access a Dictionary value?

# Answer:
# "We access a value using its key."

# Example:

# person["name"]


# Q3. Can Dictionary have duplicate keys?
#
# Answer:
# "No. Dictionary keys must be unique."


# Q4. Can Dictionary have duplicate values?
#
# Answer:
# "Yes, Dictionary values can be duplicated."


# Q5. Is Dictionary mutable?
#
# Answer:
# "Yes, Dictionary is mutable."


# Q6. How do you add data?
#
# Answer:
# person["city"] = "Bengaluru"


# Q7. How do you update data?
#
# Answer:
# person["age"] = 26


# Q8. How do you remove data?
#
# Answer:
# del person["city"]
#
# OR
#
# person.pop("city")


# ============================================================
# EASY MEMORY
# ============================================================
#
# Dictionary = KEY : VALUE
#
# person["name"]       -> get value
#
# person["city"] = ... -> add
#
# person["age"] = ...  -> update
#
# del person["city"]   -> remove
#
# get()    -> get value safely
# keys()   -> all keys
# values() -> all values
# items()  -> key + value
# pop()    -> remove
#
# IMPORTANT:
# Dictionary -> unique KEYS
# Dictionary -> duplicate VALUES allowed
#
# ============================================================