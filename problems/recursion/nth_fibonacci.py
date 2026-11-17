import sys

sys.setrecursionlimit(200000)

n = int(input())
a = {}

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in a:
        return a[n]
    a[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return a[n]

def nth_fibonacci(n):
    print(fibonacci(n))

nth_fibonacci(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/I
# 🚩 use python3 instead of pypy
