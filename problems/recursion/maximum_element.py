import sys

sys.setrecursionlimit(200000)

n = int(input())
arr = list(map(int, input().split()))

def maximum(n, arr):
    if n == 1:
        return arr[0]
    return max(maximum(n-1,arr), arr[n-1])

def maximum_element(n, arr):
    print(maximum(n, arr))

maximum_element(n, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/M
# 🚩 use python3 instead of pypy
