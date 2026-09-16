# ============================================================
# DICTIONARY - IMPORTANT CODING QUESTIONS
# ============================================================


# Q1. Print the value of a particular key
# ------------------------------------------------------------
# Kya karna hai?
# Dictionary me "name" ki value nikalni hai.

# Logic:
# Key do -> Value mil jayegi.


person = {
    "name": "Maruf",
    "age": 26
}

print(person["name"])

# Output:
# Maruf


# ============================================================
# Q2. Add a new key-value pair
# ============================================================
# Kya karna hai?
# Dictionary me city add karni hai.


person = {
    "name": "Maruf",
    "age": 26
}

person["city"] = "Bengaluru"

print(person)

# Output:
# {'name': 'Maruf', 'age': 26, 'city': 'Bengaluru'}


# ============================================================
# Q3. Update a value
# ============================================================
# Kya karna hai?
# Age ko 26 se 27 karna hai.


person = {
    "name": "Maruf",
    "age": 26
}

person["age"] = 27

print(person)

# Output:
# {'name': 'Maruf', 'age': 27}


# ============================================================
# Q4. Check if a key exists
# ============================================================
# Kya karna hai?
# Check karna hai ki "email" key Dictionary me hai ya nahi.


person = {
    "name": "Maruf",
    "age": 26
}

if "email" in person:
    print("Email exists")
else:
    print("Email does not exist")

# Output:
# Email does not exist


# ============================================================
# Q5. Print all keys
# ============================================================
# Kya karna hai?
# Dictionary ke saare keys print karne hain.


person = {
    "name": "Maruf",
    "age": 26,
    "city": "Bengaluru"
}

for key in person:
    print(key)

# Output:
# name
# age
# city


# ============================================================
# Q6. Print all values
# ============================================================
# Kya karna hai?
# Dictionary ke saare values print karne hain.


person = {
    "name": "Maruf",
    "age": 26,
    "city": "Bengaluru"
}

for value in person.values():
    print(value)

# Output:
# Maruf
# 26
# Bengaluru


# ============================================================
# Q7. Print key and value together
# ============================================================
# Kya karna hai?
# Har key ke saath uski value print karni hai.

# IMPORTANT:
# Ye interview me commonly pucha ja sakta hai.


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
# Q8. Count frequency of numbers
# ============================================================
# Kya karna hai?
# List me har number kitni baar aaya hai.

# Example:
# 10 -> 2 times
# 20 -> 2 times
# 30 -> 1 time

# Dictionary ka use karke count karenge.


numbers = [10, 20, 10, 30, 20]

count = {}

for num in numbers:

    if num in count:
        count[num] = count[num] + 1
    else:
        count[num] = 1

print(count)

# Output:
# {10: 2, 20: 2, 30: 1}


# EASY LOGIC:

# Number pehli baar mila:
# count = 1

# Same number dobara mila:
# count = count + 1


# ============================================================
# Q9. Find the largest value in Dictionary
# ============================================================
# Kya karna hai?
# Dictionary me scores hain.
# Hume sabse bada score chahiye.


marks = {
    "Ali": 70,
    "Ahmed": 85,
    "Rahul": 60
}

largest = max(marks.values())

print(largest)

# Output:
# 85


# ============================================================
# Q10. Find the smallest value
# ============================================================


marks = {
    "Ali": 70,
    "Ahmed": 85,
    "Rahul": 60
}

smallest = min(marks.values())

print(smallest)

# Output:
# 60


# ============================================================
# Q11. Find total of Dictionary values
# ============================================================
# Kya karna hai?
# Saare marks ka total chahiye.


marks = {
    "Math": 70,
    "English": 80,
    "Python": 90
}

total = sum(marks.values())

print(total)

# Output:
# 240


# ============================================================
# Q12. Remove a key
# ============================================================


person = {
    "name": "Maruf",
    "age": 26,
    "city": "Bengaluru"
}

del person["city"]

print(person)

# Output:
# {'name': 'Maruf', 'age': 26}


# ============================================================
# Q13. Copy a Dictionary
# ============================================================


person = {
    "name": "Maruf",
    "age": 26
}

new_person = person.copy()

print(new_person)

# Output:
# {'name': 'Maruf', 'age': 26}


# ============================================================
# Q14. Check if Dictionary is empty
# ============================================================


person = {}

if not person:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")

# Output:
# Dictionary is empty


# ============================================================
# Q15. Count characters in a String using Dictionary
# ============================================================
# Kya karna hai?
# String me har character kitni baar aaya hai.

# Example:
# "hello"

# h -> 1
# e -> 1
# l -> 2
# o -> 1


text = "hello"

count = {}

for char in text:

    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1

print(count)

# Output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# ============================================================
# MOST IMPORTANT MEMORY
# ============================================================

# Dictionary:

# data = {
#     "key": "value"
# }

# Get:
# data["key"]

# Add:
# data["city"] = "Bengaluru"

# Update:
# data["age"] = 27

# Remove:
# del data["age"]

# Check:
# "name" in data

# All keys:
# data.keys()

# All values:
# data.values()

# Key + Value:
# data.items()

# ============================================================