#To find whether the number is even or not
a = int(input("Please enter your number\n"))
if (a%2==0):
    print(a,"is even number\n")
else:
    print(a,"is not even number\n")

if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print(a,"is a not a prime number\n")
            break
    else:
            print(a,"is a prime number\n")
else:
    print(a,"is not a prime number\n")