'''#Matrix Addition
A = [[1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

R = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        R[i][j] = A[i][j] + B[i][j]

for r in R:
    print(r)'''

#Matrix Multiplication
A = [[2, 1, 3],
     [3, 2, 1],
     [1, 2, 3]]

B = [[4, 5, 6],
     [5, 4, 6],
     [6, 4, 5]]

R = [[0, 0, 0], 
     [0, 0, 0], 
     [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        R[i][j] = A[i][j] * B[i][j]

for r in R:
    print(r)