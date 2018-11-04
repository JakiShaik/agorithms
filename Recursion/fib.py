from collections import defaultdict

def fibonacci(n,prev={0:0,1:1}):
    if n in prev:
        return prev[n]
    prev[n] = fibonacci(n-1)+fibonacci(n-2)
    return prev[n]
    # Write your code here.

n = int(input())
print(fibonacci(n))