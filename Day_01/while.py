"""
# Q1: count digit using while loop
userInput=int(input("Enter a numbers : "))
count=0
while userInput > 0:
    userInput //= 10 
    count+=1
print(f'number of digits is {count}')
"""

"""
# Q2: sum of digits using while loop
n=5
sum=0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n //= 10
print(f'sum of digits is {sum}')
"""
"""
# Q3: reverse a number using while loop
n=1234
reverse=0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print(f'reverse of number is {reverse}')
"""


"""
# Q4: sum of even number 1 to 20
sum=0
i=1
while i <= 20:
    if i % 2 == 0:
        sum += i
    i += 1
print(f'sum of even number from 1 to 20 is {sum}')
"""


"""
# Q5: print table of a number using while loop
userNumber=int(input("Enter A number for a table : "))
i=1
while i <= 10:
    print(f'{userNumber} X {i} = {userNumber*i}')
    i += 1
"""

