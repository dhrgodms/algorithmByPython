import sys
import math
n = int(sys.stdin.readline().rstrip('\n'))
case_list = list(list(map(int,sys.stdin.readline().rstrip('\n').split()))for _ in range(n))
for i in case_list:
    D = math.sqrt((i[3]-i[0])**2+(i[4]-i[1])**2)
    if D==0 and i[2]==i[5]:
        print(-1)
    elif D<i[2]+i[5] and D>abs(i[2]-i[5]):print(2)
    elif D==i[2]+i[5] or D==abs(i[5]-i[2]):print(1)
    else: print(0)