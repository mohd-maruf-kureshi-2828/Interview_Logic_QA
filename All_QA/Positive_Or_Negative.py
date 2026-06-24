userNum=int(input("Enter a number: "))

if userNum>0:
    print(f"{userNum} is a positive number.")
elif userNum<0:
    print(f"{userNum} is a negative number.")
else:
    print(f"{userNum} is zero.")