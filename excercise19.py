#Matrix addition
rows1 = int(input("Enter the Number of rows : "))
column1 = int(input("Enter the Number of Columns: "))
rows2 = int(input("Enter the Number of rows : "))
column2 = int(input("Enter the Number of Columns: "))
if(rows1==rows2 and column1==column2):
    print("Enter the elements of First Matrix:")
    A = [[int(input()) for i in range(column1)] for i in range(rows1)]
    print("First Matrix is: ")
    for n in A:
        print(n)

    print("Enter the elements of Second Matrix:")
    B = [[int(input()) for i in range(column2)] for i in range(rows2)]
    for n in B:
        print(n)

    C = [[0 for i in range(column1)] for i in range(rows1)]

    for i in range(rows1):
        for j in range(column1):
            C[i][j] = A[i][j] + B[i][j]

    print("The Sum of Above two Matrices is : ")
    for r in C:
        print(r)
else:
    print("Matrix addition cannot be done")