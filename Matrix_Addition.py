#MAtrix Addition
#Transpose Matrix - Ith row, jth col = jth row , ith col

mat1 = [[1,5,3],[1,3,3]]
mat2 = [[2,1,3],[2,1,3]]
Sum = [[0,0,0],[0,0,0]]
Transpose = [[0,0],[0,0],[0,0]]
#------------------------------------------------------
for m1 in range(len(mat1)):
    print("Mat1:",m1)
    for m2 in range(len(mat2[0])):
        print("Mat2",m2)
        Sum[m1][m2] = mat1[m1][m2]  - mat2[m1][m2]

for i in Sum:
    print(i)
#-------------------------------------------------------------
for m1 in range(len(mat1)):
    print("Mat1:",m1)
    for m2 in range(len(mat2[0])):
        print("Mat2",m2)
        Transpose[m2][m1] = mat1[m1][m2]

for i in Transpose:
    print(i)