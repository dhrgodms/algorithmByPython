import sys

n, m = map(int,sys.stdin.readline().rstrip('\n').split())
cards_list = list(map(int,sys.stdin.readline().rstrip('\n').split()))
gap = 300000
close_total = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if m-(cards_list[i]+cards_list[j]+cards_list[k])>=0 and abs(m-(cards_list[i]+cards_list[j]+cards_list[k]))<gap:
                gap = abs(m - (cards_list[i] + cards_list[j] + cards_list[k]))
                close_total = cards_list[i] + cards_list[j] + cards_list[k]
print(close_total)
