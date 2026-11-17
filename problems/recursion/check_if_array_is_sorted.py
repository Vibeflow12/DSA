import sys

sys.setrecursionlimit(200000)

n = int(input())
arr = list(map(int, input().split()))

def is_sorted(n, arr):
    if n == 1:
        return ("YES")
    if is_sorted(n - 1, arr) == ("NO"):
        return ("NO")
    if arr[n - 1] >= arr[n - 2]:
        return ("YES")
    return ("NO")

def check_if_array_is_sorted(n, arr):
    print(is_sorted(n, arr))

check_if_array_is_sorted(n, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/O
# 🚩 use python3 instead of pypy
