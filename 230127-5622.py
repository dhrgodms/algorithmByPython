alphabet = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
str = input()
resultTime = 0
for i in range(len(str)):
    for j in range(len(alphabet)):
        if str[i] in alphabet[j]:
            resultTime += j+3
print(resultTime)