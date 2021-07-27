#Amstrong number
print("Welcome to Amstrong number checker, if the number's sum is same as the sum of the cubes of respective digits then it is called Amstrong number")
a=int(input("Please enter your number\n"))
sum=0
temp=a
while(temp >0):
    b=temp%10
    sum+=b **3
    temp//=10
if(a==sum):
    print(a,"is an Amstrong number")
else:
    print(a,"isn't an Amstrong number")
    print("It's sum for the respective digits is", sum)