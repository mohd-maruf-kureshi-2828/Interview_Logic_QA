# 🔥 FIBONACCI SEQUENCE

# 👉 Fibonacci kya hota hai?

# Fibonacci sequence mein next number

# previous 2 numbers ko add karke banta hai.

# Example:

# 0, 1, 1, 2, 3, 5, 8, 13...

#

# 0 + 1 = 1

# 1 + 1 = 2

# 1 + 2 = 3

# 2 + 3 = 5

# 👉 Code

a = 0
b = 1

# Starting ke 2 numbers

# a = 0

# b = 1

userInt = int(input("Enter the number of terms you want in Fibonacci sequence: "))

if userInt == 1:
# Agar user sirf 1 term chahta hai
  print(a)

else:
# Starting ke 2 numbers print honge
   print(a)
   print(b)
# 2 se start karenge kyunki 0 aur 1 already print ho chuke hain
   for i in range(2, userInt):

    # Next number = previous 2 numbers ka addition
         c = a + b
    # Values ko aage shift kar rahe hain
         a = b
         b = c
    # New Fibonacci number print
         print(c)

# 🎤 Interview mein bolo:

# "Fibonacci sequence is a sequence where

# each number is the sum of the previous two numbers."

# 👉 Important:

# a = first number

# b = second number

# c = next number

# c = a + b
