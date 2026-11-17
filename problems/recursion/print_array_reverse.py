import sys

sys.setrecursionlimit(200000)

n = int(input())
arr = list(map(int, input().split()))

def array_reverse(n, arr):
    if n == 0:
        return
    print(arr[n - 1],end = " ")
    array_reverse(n - 1, arr)

def print_array_reverse(n, arr):
    array_reverse(n, arr)

print_array_reverse(n, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/J
# 🚩 use python3 instead of pypy
