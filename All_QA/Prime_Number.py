num = int(input("Enter A Number To Check Prime Or Not : "))
if num <=1:
    print("Not A Prime Number ")

if num > 1 :
    for i in range(2,num):
        if num % i == 0:
            print("this is not a prime number") 
            break;
    else:
        print("this is prime number")

# Prime Number

###  Simple Samajh
"""

Prime number woh number hai jo **1 se bada** ho aur sirf **1 aur khud se divide** ho.

Example: `7` → 1 aur 7 se divide hota hai → Prime ✅

### 🎤 Interview Mein

> A prime number is a number greater than 1 that has exactly two factors: 1 and itself.


"""
num = 7
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")

