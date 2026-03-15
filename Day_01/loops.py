
"""
# print from 1 to 10
for i in range(1,11):
    print(i)
"""

"""
# print even and number from 1 to 10
for i in range(1,101):
    if i % 2 == 0:
        print(f'even number is {i}')
    else:
        print(f'odd number is {i}')
"""


"""# sum of number from 1 to n
n=5
total=0
for i in range(1,n+1):
    total+=i #total = total  + i 
print(total)

"""

"""# find the factorial
n=5
fact=1
for i in range(1,n+1):
    fact *= i # 5*4*3*2*1
print(fact)
"""


"""
# print table of a number
userNumber=int(input("Enter A number for a table : "))
for i in range(1,11):
    print(f'{userNumber} X {i} = {userNumber*i}')
"""

"""
# square rote of  a number
for i in range(1,10):
    print(i*i)
"""


"""
# reverse 1 to 10
for i in range(10,0,-1):
    print(i)
"""


"""
# sum of even number 1 to 20
sum=0
for i in range(1,21):
    if i % 2 == 0:
        sum+=i
print(sum)
"""


"""
#reverse a string
name="python developer"

# print(name[::-1])

for i in range(len(name)-1,-1,-1):
    print(name[i], end="")

for i in reversed(name):
    print(i)
"""



#find the largest number in list
numbers=[10,20,30,40,50]
largest=numbers[0] #largest = 10
for i in numbers:
    if i > largest: # 10 > 10 false 20 > 10 true 30 > 20 true 40 > 30 true 50 > 40 true
        largest = i
# print(largest)
"""
full explaination:
1. We have a list of numbers: [10, 20, 30, 40, 50].
2. We initialize a variable `largest` with the value of the first element of the list, which is 10.
3. We start a loop that iterates through each number `i` in the list.
4. In the first iteration, `i` is 10. We compare it with `largest` (which is also 10). Since 10 is not greater than 10, we do not update `largest`.
"""
# second way to find largest number in list
# largest=max(numbers)
# print(largest)




"""
# count vowels in a string
name="python"
count=0
for ch in name:
    if ch in 'aeiou':
        count+=1
print(count)
"""

#fibonacci series
a=0
b=1
for i in range(10):
    # print(a,end=" ")
    temp = a
    a = b
    b = temp + b


"""
check the prime number
number=7
count=0
for i in range(1,number+1):
    if number % i == 0:
        count+=1

if count == 2:
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
"""

