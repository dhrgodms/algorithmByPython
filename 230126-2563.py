n = int(input())
matrix = [['X']*101 for _ in range(101)]
for _ in range(n):
    row,col = map(int,input().split())
    for i in range(10):
        for j in range(10):
            matrix[row+i][col+j] = 'O'

result = 0
for i in range(100):
    result += matrix[i].count('O')
print(result)