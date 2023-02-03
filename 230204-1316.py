n = int(input())
str = list(input() for _ in range(n))
result = 0
str_index = []
successed = True
for i in str:
    for j in range(len(i)):
        if i[j] in str_index and j!=0:
            if i[j-1]!=i[j]:
                successed = False
                break
        else:
            str_index.append(i[j])
            successed = True
    if successed : result += 1
    str_index = []
print(result)