import sys
n,m = map(int, sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))
sum_list = [0]
sum, j = 0,0
for i in n_list:
    sum += i
    sum_list.append(sum)
while m>j:
    start, end = map(int,sys.stdin.readline().split())
    print(sum_list[end]-sum_list[start-1])
    j += 1