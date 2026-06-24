# 🔥 LEAP YEAR PROGRAM

# 👉 Leap year kya hota hai:
# 366 days wala year (Feb me 29 days)

# 👉 Rules:
# 1. 400 se divisible → Leap year
# 2. 100 se divisible but 400 nahi → Not leap
# 3. 4 se divisible but 100 nahi → Leap

year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year.")

elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year.")

else:
    print(f"{year} is not a leap year.")

# 👉 Important:
# % (modulus) remainder check karta hai
# == 0 matlab perfectly divisible

"""
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

"""