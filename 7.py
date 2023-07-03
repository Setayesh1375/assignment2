

n = int(input("Enter length of Fibonacci series: "))
num1 =0
num2 = 1
num3 = 1
i = 1

while(i <= n):
    if n==2:
        print("1","1")
        break
    print( num3, end=" ")
    i += 1
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    