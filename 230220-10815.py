import sys

n = int(sys.stdin.readline().rstrip('\n'))
n_list = list(map(int,sys.stdin.readline().rstrip('\n').split()))
m = int(sys.stdin.readline().rstrip('\n'))
m_list = list(map(int,sys.stdin.readline().rstrip('\n').split()))

n_list.sort()

for i in m_list:
    start,mid,end=0,(n-1)//2,n-1
    while end-start>1:
        if i < n_list[mid]:
            end = mid
            mid = end - (end-start)//2
        elif i > n_list[mid]:
            start = mid
            mid = start+(end-start)//2
        else:
            print(1, end=" ")
            break;
    if end-start==1:
        if n_list[start]!=i and n_list[end]!=i: print(0, end=" ")
        else : print(1, end=" ")
