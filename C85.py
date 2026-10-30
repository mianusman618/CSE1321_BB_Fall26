mat_A=[[1,2,3],[4,5,6]]
mat_B=[[7,8,9],[10,11,12]]
print("Matrix A: ")
for row in mat_A:
    for value in row:
        print(value,end=" ")
    print()
print("Matrix B: ")
for i in range(len(mat_B)):
    for j in range(len(mat_B[0])):
        print(mat_B[i][j],end=" ")
    print()
mat_C=[]
for i in range(len(mat_B)):
    row=[]
    for j in range(len(mat_B[0])):
        row.append(mat_A[i][j]+mat_B[i][j])
    mat_C.append(row)
print("Matrix C: ")
for row in mat_C:
    for value in row:
        print(value,end=" ")
    print()