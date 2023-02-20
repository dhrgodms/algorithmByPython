n = int(input())
result = ""
for i in range(1,int(n/4)+1):
    if i != (n/4):
        result += "long "
    else:
        result += "long int"
print(result)
