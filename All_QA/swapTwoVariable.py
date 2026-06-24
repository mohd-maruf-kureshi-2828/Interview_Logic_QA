# 🔥 SWAPPING WITHOUT TEMP VARIABLE (PYTHON SHORTCUT)

# 👉 initial values
num1 = 20
num2 = 30

# 👉 swapping using left-right concept (tuple unpacking)
num1, num2 = num2, num1

# 👉 kaise kaam karta hai:
# right side pe values ek tuple banati hai
# (num2, num1) → (30, 20)

# fir left side me assign hota hai:
# num1 = 30
# num2 = 20

# 👉 final result:
# num1 = 30
# num2 = 20

# 👉 print output
print("After swapping: num1 =", num1)
print("After swapping: num2 =", num2)

# 👉 Important:
# ye method fast hai, clean hai aur interview me best hai


# 🔥 SWAPPING USING TEMP VARIABLE

# 👉 swapping ka matlab:
# do variables ki value exchange karna

x = 90
y = 100

# step 1: temp me x store karo
temp = x   # temp = 90

# step 2: x me y daalo
x = y      # x = 100

# step 3: y me temp daalo
y = temp   # y = 90

# 👉 final:
# x = 100
# y = 90

# print output
print(f'the value of x is : {x}')
print(f'the value of y is : {y}')

# 👉 Important:
# temp variable ek temporary storage hota hai
# use karte hai jab direct swap possible na ho