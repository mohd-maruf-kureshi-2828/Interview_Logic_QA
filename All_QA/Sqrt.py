# find the square root of a number using the exponentiation operator
def sqrt(n):
    return n ** 0.5

# print(sqrt(64))

# without funtion
n=64
sqrt=n ** (1/2)
# print(sqrt)

# using import math
import math
mathSqrt=math.sqrt(9)
# print(mathSqrt)

userInt=int(input("Enter a number to find the square root : "))
sqrt=userInt**(1/2)
# print(f'square root of {userInt} is {sqrt}')



# 🔥 SQUARE ROOT (√) NOTES

# 👉 Square root ka matlab:
# Aisa number jo khud se multiply hone par original number de

# Example:
# 3 * 3 = 9 → √9 = 3
# 4 * 4 = 16 → √16 = 4

# 👉 Formula:
# x^2 = x * x  (square)
# √x = reverse of square (square root)

# 👉 Python me square root nikalne ke 2 tarike:

# Method 1: math module use karke
import math
num = 36
print(math.sqrt(num))   # Output: 6.0

# Method 2: power use karke exponentiation operator se
num = 49
print(num ** 0.5)       # Output: 7.0

# 👉 Important:
# √25 = 5 (programming me positive value use hoti hai)

# 👉 Use cases:
# - Maths calculation
# - Distance formula
# - Games & graphics
# - AI / ML

# 👉 Example program:
num = int(input("Enter a number: "))
sqrt = num ** 0.5
print("Square root is:", sqrt)


