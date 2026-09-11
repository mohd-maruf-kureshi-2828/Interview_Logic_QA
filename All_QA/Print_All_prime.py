startNum=int(input("enter a number to start from: "))
endN=int(input("enter a number to end at: "))

for num in range(startNum,endN+1):
    for i in range(2,num):
        if num % i == 0:
            break;
    else:
        print(num)