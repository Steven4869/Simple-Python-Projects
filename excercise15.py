#To print multiplication table until 10 counts
num = int(input("Please enter your number\n"))
if(num<0):
    print("invald input\n")
else:
    print("Multiplication table until 10 counts for", num)
    for i in range(1,11):
        print(num*i,end=" ")
