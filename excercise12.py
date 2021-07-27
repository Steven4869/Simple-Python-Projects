#to print the lenght of the string
a="In all chaotic beauty lies a wounded work of art\n Beautiful but torn, wreaking havoc on my heart \nCamouflaged by insecurities, blinded by it all\nI love the way you sit there and barely notice me at all"
print("length of poem\n",a,"\nis",len(a))
b=input("Please enter the word from poem\n")
if(b in a):
    print("yes, the word",b,"is there in poem")
else:
    print("no, the word",b," is not there in poem")