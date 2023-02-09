import sys

n = int(sys.stdin.readline())
numberList= [0]*10001

for i in range(n):
    numberList[int(sys.stdin.readline())] += 1

for i in range(len(numberList)):
    if numberList[i] != 0:
        for _ in range(numberList[i]):
            print(i)