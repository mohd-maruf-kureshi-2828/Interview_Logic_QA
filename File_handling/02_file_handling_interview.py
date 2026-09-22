# ==========================================
# FILE HANDLING - MNC / STARTUP INTERVIEW
# ==========================================


# ==========================================
# THEORY INTERVIEW QUESTIONS
# ==========================================


# Q1. What is file handling in Python?
#
# Answer:
# File handling is used to read, write,
# append and manage data in files.


# ------------------------------------------


# Q2. Which function is used to open a file?
#
# Answer:
# open() function is used to open a file.


# ------------------------------------------


# Q3. What are the common file modes?
#
# Answer:
# r -> read
# w -> write
# a -> append


# ------------------------------------------


# Q4. What is the difference between
# "r" and "w" mode?
#
# Answer:
# "r" is used to read a file.
# "w" is used to write data and can
# overwrite existing data.


# ------------------------------------------


# Q5. What is the difference between
# "w" and "a" mode?
#
# Answer:
# "w" can overwrite existing data,
# while "a" adds new data at the end.


# ------------------------------------------


# Q6. What does read() do?
#
# Answer:
# read() reads the complete content
# of a file.


# ------------------------------------------


# Q7. What does readlines() do?
#
# Answer:
# readlines() reads the lines of a file
# and returns them as a list.


# ------------------------------------------


# Q8. What does write() do?
#
# Answer:
# write() is used to write data
# into a file.


# ------------------------------------------


# Q9. Why do we use close()?
#
# Answer:
# close() closes the file and releases
# the resources used by the file.


# ------------------------------------------


# Q10. What is the advantage of
# "with open()"?
#
# Answer:
# with open() automatically closes
# the file after the operation is complete.


# ------------------------------------------


# Q11. What happens if we open a file
# in "w" mode?
#
# Answer:
# Existing content can be overwritten.


# ------------------------------------------


# Q12. What happens if we open a file
# in "a" mode?
#
# Answer:
# New data is added at the end of
# the existing content.


# ------------------------------------------


# Q13. What is the difference between
# read() and readlines()?
#
# Answer:
# read() returns the complete file content
# as a string.
#
# readlines() returns the lines as a list.


# ------------------------------------------


# Q14. What happens if we try to open
# a file that does not exist in "r" mode?
#
# Answer:
# Python raises FileNotFoundError.


# ==========================================
# CODING QUESTIONS
# ==========================================


# Q1. Read and print a file
# ------------------------------------------

with open("notes.txt", "r") as file:
    data = file.read()
    print(data)


# ------------------------------------------
# Q2. Write data into a file
# ------------------------------------------

with open("test.txt", "w") as file:
    file.write("Hello Python")


# ------------------------------------------
# Q3. Append data to a file
# ------------------------------------------

with open("test.txt", "a") as file:
    file.write("\nLearning Django")


# ------------------------------------------
# Q4. Handle FileNotFoundError
# ------------------------------------------

try:
    with open("abc.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File not found")


# Output:
# File not found


# ------------------------------------------
# Q5. Count lines in a file
# ------------------------------------------

with open("notes.txt", "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))


# ------------------------------------------
# Q6. Read file line by line
# ------------------------------------------

with open("notes.txt", "r") as file:

    for line in file:
        print(line.strip())


# ==========================================
# QUICK INTERVIEW REVISION
# ==========================================

# open()      -> open file
# read()      -> read complete data
# readlines() -> read lines as list
# write()     -> write / overwrite
# append      -> add at end
# close()     -> close file
# with open() -> automatically close
# FileNotFoundError -> file does not exist


# ==========================================
# MOST IMPORTANT FOR FRESHER
# ==========================================

# Interviewer agar bole:
#
# "Read a file"
#
# Use:
#
# with open("file.txt", "r") as file:
#     data = file.read()
#     print(data)
#
#
# Interviewer agar bole:
#
# "Append data"
#
# Use:
#
# with open("file.txt", "a") as file:
#     file.write("New data")