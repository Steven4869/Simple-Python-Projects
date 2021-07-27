#Sum of first 100 even numbers using for loop
# num=200
total=0
for i in range(1,202):
    if((i%2)==0):
        total=total+i
print("sum of first 100 even numbers is ", total)