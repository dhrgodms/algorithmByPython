alphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
input_char = input()
result = 0
for i in alphabet:
    if i in input_char:
        result += input_char.count(i)
        input_char = input_char.replace(i,'?')
input_char = input_char.replace('?','')
print(result+len(input_char))