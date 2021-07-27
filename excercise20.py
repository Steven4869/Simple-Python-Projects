#Matrix multipliaction
rows1 = int(input("Enter the Number of rows : "))
column1 = int(input("Enter the Number of Columns: "))
rows2 = int(input("Enter the Number of rows : "))
column2 = int(input("Enter the Number of Columns: "))
if(rows1==column2):
    print("Enter the elements of First Matrix:")
    A = [[int(input()) for i in range(column1)] for i in range(rows1)]
    print("First Matrix is: ")
    for n in A:
        print(n)

    print("Enter the elements of Second Matrix:")
    B = [[int(input()) for i in range(column2)] for i in range(rows2)]
    print("Second Matrix is: ")
    for n in B:
        print(n)
    C = [[0 for i in range(column2)] for i in range(rows1)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    print("The resultant matrix is:")
    for r in C:
        print(r)
else:
    print("Matrix multiplication is not possible")