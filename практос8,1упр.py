N = 3
M = 4

A = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9,10,11,12]]

for i in range(N):
    tmp = A[i][0]
    A[i][0] = A[i][M-1]
    A[i][M-1] = tmp

for i in range(N):
   for j in range(M):
      print("%2d " % A[i][j], end='')
print()

# 
