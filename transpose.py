A = [[2, 3, 1],
     [3, 4, 2]]

R = [[0, 0],
     [0, 0],
     [0, 0]]
    
for i in range(len(A)):
    for j in range(len(A[0])):
        R[j][i] = A[i][j]

for r in R:
    print(r)