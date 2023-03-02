n,m = map(int, input().split())
basket = [0]*n
for _ in range(m):
    i,j,k = map(int, input().split())
    for h in range(i,j+1):
        basket[h-1] = k
for i in basket:
    print(i, end=" ")