import sys

n,m = map(int,input().split())
str_list = set([])
result = 0
for _ in range(n):
    str_list.add(sys.stdin.readline().rstrip('\n'))
for _ in range(m):
    input_str =sys.stdin.readline().rstrip('\n')
    if input_str in str_list:
        result += 1
print(result)
