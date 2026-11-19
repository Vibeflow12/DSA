import sys

sys.setrecursionlimit(2000000)

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def occurance(n, arr, x):
    if n == 0:
        return -1

    smallans = occurance(n - 1, arr, x)

    if smallans != -1:
        return smallans

    if arr[n - 1] == x:
        return n

    return -1

def first_occurance_of_x(n, arr, x):
    print(occurance(n, arr, x))

first_occurance_of_x(n, arr, x)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/P
# 🚩 use python3 instead of pypy
