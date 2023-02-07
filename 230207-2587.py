num_list = list(int(input()) for _ in range(5))
num_list.sort()
total = 0
for i in range(5):
    total += num_list[i]
print(int(total/5))
print(num_list[2])