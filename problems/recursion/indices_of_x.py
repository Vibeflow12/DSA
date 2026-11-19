import sys

sys.setrecursionlimit(2000000)

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def occurance(n, arr, x):
    if n == 0:
        return 0

    smallans = occurance(n - 1, arr, x)

    if arr[n - 1] == x:
        print(n,end = " ")
        return smallans + 1

    return smallans

def indices_of_x(n, arr, x):
    if occurance(n, arr, x) ==0 :
        print(-1)
    else:
        print()

indices_of_x(n, arr, x)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/R
# 🚩 use python3 instead of pypy
