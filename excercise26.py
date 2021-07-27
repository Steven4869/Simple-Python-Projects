#Write in the text file
f=open("cell.txt","w")
f.write("Welcome to my project\n")
f.write("This method allows us to only write in the file\n")
f.close()
#Append in the text file
f=open("cell.txt","a")
f.write("This will append the tex given")
f.close()
#Read in the text file
f=open("cell.txt","r+")
# print(f.read())
# print(f.read(5))
print(f.readlines())