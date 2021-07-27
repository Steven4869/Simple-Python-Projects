#Fibonacci series using while loop
terms=int(input("Please enter the number of terms for fibonacci sequence\n"))
first,second=0,1
i=0
if (terms<=0):
    print("Invalid input")
elif (terms==1):
    print(first)
else:
    print("Fibonacci series upto", terms, "terms\n")
    while (i<terms):
        print(first,end=" ")
        next=first+second
        first=second
        second=next
        i=i+1
