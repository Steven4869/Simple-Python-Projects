p=input("Enter first string:")
q=input("Enter second string:")
a=list(set(p)&set(q))
print("The common letters are:")
for i in a:
    print(i)
