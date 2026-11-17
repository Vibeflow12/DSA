import sys

sys.setrecursionlimit(200000)

x,n = map(int,input().split())

def power_recursion(x,n):
    if n == 0:
        return 1
    return x * power_recursion(x,n - 1)

def power(x,n):
    print(power_recursion(x,n))
power(x,n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/G
# 🚩 use python3 instead of pypy
