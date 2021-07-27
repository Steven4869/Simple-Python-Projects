#Calculator to perform the basoc operations
print("Please select the operation\n")
print(" 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Divison\n")
choice=int(input("Please enter your desired operation\n"))
num1=float(input("Please enter your first number: "))
num2=float(input("Please enter your second number: "))
if(choice==1):
    print("Sum of the numbers ",num1,",",num2,"is", num1 + num2)
elif(choice==2):
    print("Subtraction of of the numbers ",num1,",",num2,"is", num1 - num2)
elif(choice==3):
    print("Multiplication of two numbers",num1,",",num2,"is", num1 * num2)
elif(choice==4):
    print("Divison of two numbers",num1,",",num2,"is", num1 / num2)
else:
    print("Invalid choice")