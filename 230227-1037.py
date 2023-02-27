import sys
n = int(input())
N_list = list(map(int,sys.stdin.readline().rstrip("\n").split()))

N_list.sort()
print(N_list[0]*N_list[-1])