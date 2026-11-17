import sys

sys.setrecursionlimit(20000)

n = int(input())

def factorial(num):
    if num == 0:
        return 1
    smallno = factorial(num - 1)
    ans = num * smallno
    return ans

def print_factorial(n):
    print(factorial(n))

print_factorial(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/E
# 🚩 use python3 instead of pypy
