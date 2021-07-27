#To create a file and write some contents. take input from user and read that many lines
file1=open("excercise40.txt","r+")
file1.write("Hello World\n")
readLINE=(int(input("Please enter the number of line you want to read\n")))
print(file1.read(readLINE))
file1.close()