n,m = map(int,input().split())

matrix1 = [list(map(int,input().split())) for _ in range(n)]
matrix2 = [list(map(int,input().split())) for _ in range(n)]
result = []

for i in range(n):
    result.append([])
    for j in range(m):
        result[i].append(matrix1[i][j]+matrix2[i][j])

for i in result:
    for j in range(m):
        print(i[j], end=" ")
    print('')