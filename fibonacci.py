''' Fibonacci series is start with two natural value 0 and 1
last two value addition in fibonacci series
i.e 0 1 1 2 3 5 8 13 21 34 55 88 you continue with addtion of last two value'''

n=int(input("Enter N : "))
a,b=0,1
while b<n:
    print(b,end=" ")
    a,b=b,a+b
print("***************************")

n=100
a,b=0,1
while b<n:
    print(b,end=" ")
    a,b=b,a+b
