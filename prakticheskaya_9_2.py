B = []
with open('E:\python\практическая 9\\практическая 9.2.1.txt','r') as f:
    for line in f.readlines():
        b=line.replace('\n','').split()
        for i in range(len(b)):
            b[i]=int(b[i])
        B.append(b)
    print(B)
print('Исходный:')
for i in range(len(B)):
    for j in range(len(B[i])):
        print(B[i][j],' ',end='')
    print()
m=len(B)
n=len(B[i])
for i in range(m):
    for j in range(n):
        min_b = min(B[i])
        a = B[i].index(min(B[i]))
    tmp1 = B[i][0]
    B[i][0] = B[i][a]
    B[i][a] = tmp1
for i in range(m):
    for j in range(n):
        max_b = max(B[i])
        b = B[i].index(max(B[i]))
    tmp2 = B[i][n-1]
    B[i][n-1] = B[i][b]
    B[i][b] = tmp2
print('Новая матрица: ')
for i in range(m):
    for k in range(n):
        print(B[i][k], end=' ')
    print()
with open('E:\python\практическая 9\\практическая 9.2.2.txt','w') as t:
    for i in range(m):
        for k in range(n):
            t.write(str(B[i][k])+' ')
        t.write('\n')