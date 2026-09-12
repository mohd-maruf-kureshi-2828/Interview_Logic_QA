"""
numEnt=int(input("Enter a number to find factorial: "))
fact=1

if numEnt<0:
    print("Factorial does not exist for negative numbers")
elif numEnt==0:
    print("The factorial of 0 is 1")

if numEnt>1:
    for i in range(1,numEnt+1):
        fact*=i

print(fact)
"""




#recursion
def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)

num=int(input("Enter a number to find factorial: "))
fact=fact(num)
print(f"The factorial of {num} is {fact}")