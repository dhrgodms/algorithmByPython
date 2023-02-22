import sys

n = int(sys.stdin.readline().rstrip('\n'))
number = [0]*8001
num_list = []
mean, center, max_idx, min_idx = 0,-1,0,0
check_num = n//2
for _ in range(n):
    number[int(sys.stdin.readline())+4000] += 1
for i in range(len(number)):
    mean += (i-4000)*number[i]
    if number[i] != 0:
        check_num -= number[i]
        if center==-1 and check_num < 0:
            center = i-4000
print(round(mean/n))
print(center)
max_num = max(number)
if number.index(max_num)+number[::-1].index(max_num) != 8000:
    print(number[number.index(max_num)+1:].index(max_num)+number.index(max_num)-3999)
else:
    print(number.index(max_num)-4000)
for idx,val in enumerate(number[::-1]):
    if val != 0:
        max_idx = idx
        break
for idx,val in enumerate(number):
    if val != 0:
        min_idx = idx
        break
print(8000-max_idx-min_idx)