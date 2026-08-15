r1=int(input("Enter the size of row of matrix A : \n"))
c1=int(input("Enter the size of column of matrix A : \n"))
r2=int(input("Enter the size of row of matrix B : \n"))
c2=int(input("Enter the size of column of matrix B : \n"))
matrix1=[]
matrix2=[]
print("\nEnter the elements in Matrix A : \n")

for i in range(r1):
    row1=[]
    for j in range(c1):
         a=int(input(f"Rows {i+1},COLUMNS{j+1}:"))
         row1.append(a)
    matrix1.append(row1)

for row1 in matrix1:
     print(row1)

print("\nEnter the elements in Matrix B : \n")

for i in range(r2):
    row2=[]
    for j in range(c2):
         b=int(input(f"Rows {i+1},COLUMNS{j+1}:"))
         row2.append(b)
    matrix2.append(row2)

for row2 in matrix2:
     print(row2)




if c1 !=r2:
     print("\nError: Matrix multiplication is not possible ")

result=[]
for i in range(r1):
     row=[]
     for j in range(c2):
          row.append(0)
     result.append(row)

for i in range(r1):
     for j in range(c2):
          for k in range(c1):
               result[i][j]+=matrix1[i][k]*matrix1[k][j]

print("\n\nThe multiplication of matrix A and B is :\n")
for row in result:
     print(row)