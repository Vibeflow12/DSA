import sys

sys.setrecursionlimit(2000000)

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def occurance(n, arr, x):
    if n == 0:
        return -1

    if arr[n - 1] == x:
        return n

    smallans = occurance(n - 1, arr, x)

    return smallans

def last_occurance_of_x(n, arr, x):
    print(occurance(n, arr, x))

last_occurance_of_x(n, arr, x)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/Q
# 🚩 use python3 instead of pypy
