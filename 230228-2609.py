# n1, n2 = map(int,input().split())
# origin_n1, origin_n2 = n1,n2
# n1_list = [0]*10001
# n2_list = [0]*10001
# i,j = 2,2
#
# while True:
#     if n1%i == 0:
#         n1_list[i] += 1
#         n1 //= i
#     elif n1 // i != 1:
#         i += 1
#
#     if n2%j == 0:
#         n2_list[j] += 1
#         n2 //= j
#     elif n2 // j != 1:
#         j += 1
#
#     if n1//i == 1 and n2 // j ==1:
#         n1_list[n1] += 1
#         n2_list[n2] += 1
#         break
#
# nn_list = []
#
# for idx, val in enumerate(n1_list):
#     if val != 0 and n2_list[idx] != 0:
#         nn_list.append(idx)
#
# maxnum, minnum = 1, 1
# if nn_list!=[]:
#     for i in nn_list:
#         maxnum *= i**min(n1_list[i],n2_list[i])
#         minnum *= i**max(n1_list[i],n2_list[i])
#     print(maxnum, minnum)
# else:
#     print(1, origin_n1*origin_n2)

maxnum, minnum = 0,0
n_list= list(map(int,input().split()))
n1, n2 = n_list[0], n_list[1]
n_list.sort()
while True:
    if n_list[1]%n_list[0] != 0:
        tmp = n_list[0]
        n_list[0] = n_list[1]%n_list[0]
        n_list[1] = tmp
        n_list.sort()
    else:
        minnum = n_list[0]
        break
print(minnum, n1*n2//minnum)


