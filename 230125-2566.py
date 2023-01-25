matrix = [list(map(int,input().split())) for _ in range(9)]
max = 0
for i in range(9):
    for j in range(9):
        if max <= matrix[i][j]:
            max = matrix[i][j]
            idxX = i
            idxY = j
print(max)
print(idxX+1,idxY+1)
