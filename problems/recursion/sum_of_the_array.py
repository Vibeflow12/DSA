import sys

sys.setrecursionlimit(200000)

n = int(input())
arr = list(map(int, input().split()))

def soa(n, arr):
    if n == 0:
        return 0
    return soa(n-1,arr) + arr[n-1]

def sum_of_the_array(n, arr):
    print(soa(n, arr))

sum_of_the_array(n, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/N
# 🚩 use python3 instead of pypy
