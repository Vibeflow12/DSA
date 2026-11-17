import sys

sys.setrecursionlimit(200000)

n = int(input())
arr = list(map(int, input().split()))

def minimum(n, arr):
    if n == 1:
        return arr[0]
    return min(minimum(n-1,arr), arr[n-1])

def minimum_element(n, arr):
    print(minimum(n, arr))

minimum_element(n, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/L
# 🚩 use python3 instead of pypy
