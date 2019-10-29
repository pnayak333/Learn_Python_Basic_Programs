#Matrix Multiplication

x = [[1,1,1],
     [2,1,1],
     [3,1,1]]
y = [[2,2,2,2],
     [3,4,5,6],
     [2,2,2,2]]

Res = [[0,0,0,0],
       [0,0,0,0,],
       [0,0,0,0,]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            Res[i][j] = Res[i][j] + (x[i][k] * y[k][j])
for i in Res:
    print(i)