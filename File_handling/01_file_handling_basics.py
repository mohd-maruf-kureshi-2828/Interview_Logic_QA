# ==========================================
# FILE HANDLING - BASIC
# ==========================================


# THEORY:
# File Handling ka use Python me files ke
# data ko read, write aur update karne ke
# liye hota hai.
#
# Common file operations:
#
# open   -> file open karna
# read   -> data read karna
# write  -> data likhna
# append -> existing data ke end me add karna
# close  -> file close karna


# ==========================================
# 1. OPEN A FILE
# ==========================================

# open() file ko open karta hai.

file = open("notes.txt", "w")

print(file)

file.close()


# ==========================================
# 2. READ A FILE
# ==========================================

# "r" = read mode

file = open("notes.txt", "r")

data = file.read()

print(data)

file.close()

# Output:
# Hello Maruf
# Python is easy
# I am learning Django


# ==========================================
# 3. READLINES
# ==========================================

# readlines() file ki lines ko
# list ke form me return karta hai.

file = open("notes.txt", "r")

data = file.readlines()

print(data)

file.close()

# Output:
# ['Hello Maruf\n',
#  'Python is easy\n',
#  'I am learning Django']


# ==========================================
# 4. WRITE TO A FILE
# ==========================================

# "w" = write mode
#
# IMPORTANT:
# w mode purana data replace/overwrite
# kar sakta hai.

file = open("notes.txt", "w")

file.write("Hello Python")

file.close()


# Ab notes.txt me:
#
# Hello Python


# ==========================================
# 5. APPEND TO A FILE
# ==========================================

# "a" = append mode
#
# Append existing data ko delete nahi karta.
# New data end me add karta hai.

file = open("notes.txt", "a")

file.write("\nI am learning Django")

file.close()


# File me ab:
#
# Hello Python
# I am learning Django


# ==========================================
# 6. CLOSE A FILE
# ==========================================

# close() file ko close karta hai.

file = open("notes.txt", "r")

print(file.read())

file.close()


# ==========================================
# 7. WITH OPEN
# ==========================================

# Python me commonly with open() use kiya jata hai.
#
# Iska benefit:
# File automatically close ho jati hai.

with open("notes.txt", "r") as file:

    data = file.read()

    print(data)


# Hume manually close() karne ki zarurat nahi.


# ==========================================
# 8. FILE MODES
# ==========================================

# "r" -> Read
# "w" -> Write
# "a" -> Append
#
# Easy Memory:
#
# r = read
# w = write
# a = add


# ==========================================
# 9. BASIC FILE HANDLING FLOW
# ==========================================

# Step 1 -> Open file
#
# Step 2 -> Read / Write / Append
#
# Step 3 -> Close file
#
# with open() use karoge to file
# automatically close ho jati hai.


# ==========================================
# EASY MEMORY
# ==========================================

# open()       -> file open
# read()       -> pura data read
# readlines()  -> lines ko list me read
# write()      -> data write/replace
# append "a"   -> end me data add
# close()      -> file close
# with open()  -> automatically close


# ==========================================
# IMPORTANT
# ==========================================

# "w" mode use karte waqt careful rehna.
# Ye existing file ka data overwrite kar sakta hai.
#
# "a" mode existing data ko preserve karke
# end me new data add karta hai.