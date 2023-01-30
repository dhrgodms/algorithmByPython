import math
bag = int(input())
result = -1

for i in range(math.ceil(bag/3)+1):
    for j in range(math.ceil(bag/5)+1):
        if bag==(5*j)+(3*i) and (result > i+j or result==-1) :
            result = i+j
            break
    if result != -1:
        break
print(result)
'''
1. 5의 배수인 경우
2. 3의 배수인 경우
3. 15의 배수인 경우
4. 5와 3의 조합으로 이루어진 경우
=> 소인수분해?!
'''