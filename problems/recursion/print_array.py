import sys

sys.setrecursionlimit(200000)

n = int(input())
arr = list(map(int, input().split()))

def array(n, arr):
    if n == 0:
        return
    array(n - 1, arr)
    print(arr[n - 1],end = " ")

def print_array(n, arr):
    array(n, arr)

print_array(n, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/K
# 🚩 use python3 instead of pypy
