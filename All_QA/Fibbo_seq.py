a=0
b=1
userInt=int(input("Enter the number of terms you want in Fibonacci sequence: "))

if userInt == 1 :
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,userInt):
        c=a+b
        a=b
        b=c
        print(c)
