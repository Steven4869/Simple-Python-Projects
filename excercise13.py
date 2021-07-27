#Palindrome printing
a=input("Please enter your word\n")
if(a==a[::-1]):
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")
