import sys

n = int(sys.stdin.readline().rstrip('\n'))
n_list = list(map(int,sys.stdin.readline().rstrip('\n').split()))
m = int(sys.stdin.readline().rstrip('\n'))
m_list = list(map(int,sys.stdin.readline().rstrip('\n').split()))
result_list = []
for i in m_list:
    if i in n_list:
        result_list.append(1)
    else:
        result_list.append(0)
for i in result_list:
    print(i, end=" ")
