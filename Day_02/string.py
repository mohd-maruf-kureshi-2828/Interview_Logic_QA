"""
# Q1 : Reverce a string
userString = input("Enter a string : ")
# print(userString[::-1])
for i in range(len(userString)-1,-1,-1):
    print(userString[i],end="")
"""
"""
# Q2 : check the string is palindrome or not
userStr=input("enter name to check is palindrome or not : ")
rev=userStr[::-1]
if userStr == rev:
    print(f'{userStr} is a palindrome string')
else:
    print(f'{userStr} is not a palindrome string')
"""


"""
# Q3 : count the vowels in string

name=input("enter your name to find the vowels : ")
count = 0
for ch in name:
    if ch in 'aeiou':
        count += 1
print(f'total vowels are : {count}')
"""

"""
#Q4 : count consonants
name=input("enter your name to find the consonents : ")
count = 0
for ch in name:
    if ch not in 'aeiou':
        count += 1
print(f'total consonants {count}')

"""

"""
# Q5 : count the total characters
name='kureshi'
count = 0
for ch in name:
   count += 1
# print(count)

# second way
print(len(name))

"""
"""
# Q6 : remove space
name="maruf kureshi is a python developer"
returnVal=name.replace(" ","") #replace return the value
print(returnVal)

"""

"""
#Q7 count the words

wolds='python is a easy language'
returnVa=wolds.split()
print(len(returnVa))
"""
"""
# Q8 :convert string into a upper case
name="maruf"
nameUpper=name.upper()
print(nameUpper)
"""

"""
# Q9 :convert into lower
name="Maruf"
lowerName=name.lower()
print(lowerName)
"""
"""
#Q10 : count the number of times a word is repeated in a string
name="python is a easy language and python is a popular language"
count = name.count("python")
print(count)
"""

"""
# Q 11 : anagram check anagram means same letter but words different
l1='listen'
l2='silent'
# print(sorted(l1))
# print(sorted(l2))

if sorted(l1) == sorted(l2):
    print('Anagram')
else:
    print('not anagram')
"""

# string compresion
name="maruf kureshi"
count = 1
for i in range(len(name)-1):
    if name[i] == name[i+1]:
        count += 1
    else:
        print(name[i]+str(count),end="")
        count = 1
print(name[-1]+str(count))