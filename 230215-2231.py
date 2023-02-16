import sys

m = int(sys.stdin.readline().rstrip('\n'))
least = m
for i in range(1,m+1):
    result = i
    for j in range(len(str(i))):
        result += int(str(i)[j])
    if result == m and least>i:
        least = i
if least == m :
    least = 0
print(least)