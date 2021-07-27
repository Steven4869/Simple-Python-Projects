#Transpose of a matrix
rows1 = int(input("Enter the Number of rows : "))
column1 = int(input("Enter the Number of Columns: "))
print("Enter the elements of your Matrix:")
A = [[int(input()) for i in range(column1)] for i in range(rows1)]
print("Matrix is: \n")
for n in A:
    print(n)
result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print("The transpose of the matrix is\n")
for r in result:
   print(r)