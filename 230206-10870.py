def fibonacchi(n):
    if n<=1:
        return n
    return fibonacchi(n-1)+fibonacchi(n-2)

n = int(input())
print(fibonacchi(n))