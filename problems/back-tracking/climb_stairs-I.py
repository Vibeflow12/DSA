import sys

sys.setrecursionlimit(20000)

n = int(input())

curr = []
ans = []

def climb(pos):
    if pos == n:
        ans.append(curr[:])
        return

    if pos > n:
        return

    curr.append(1)
    climb(pos + 1)
    curr.pop()

    curr.append(2)
    climb(pos + 2)
    curr.pop()

def climb_stairs_one(n):
    climb(0)

    for i in ans:
        print(" ".join(map(str, i)))

climb_stairs_one(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733753/problem/A
# 🚩 use python3 instead of pypy
