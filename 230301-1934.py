n = int(input())
i = 0
while i<n:
    gcd = 0
    n1,n2 = map(int, input().split())
    for g in range(1, max(n1,n2)+1):
        if n1%g==0 and n2%g==0:
            gcd = g
    i += 1
    print(n1*n2//gcd)