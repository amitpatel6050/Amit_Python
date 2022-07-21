'''if number is divide with 1 and self then number is prime
even number is not prime number'''

n=int(input("Enter N : "))
if n%2==0:
    print(n," Is not Prime")
else:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n,"Is not Prime")
            break
    else:
        print(n," IS Prime")
