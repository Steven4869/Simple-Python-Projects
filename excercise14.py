#To print facctorial for dirst 20 natural even numbers
num=2
f=1
while(num<=40):
    for i in range(1,num+1):
        f=f*i
    print("Factorial of",num,"is",f)
    f=1
    num=num+2

