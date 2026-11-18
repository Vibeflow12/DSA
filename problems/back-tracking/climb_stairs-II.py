import sys

sys.setrecursionlimit(20000)

n,k = map(int,input().split())

curr = []
ans = []

def climb(pos):
    if pos == n:
        ans.append(curr[:])
        return

    if pos > n:
        return

    for jump in range(1, k + 1):
        curr.append(jump)
        climb(pos + jump)
        curr.pop()

def climb_stairs_two(n):
    climb(0)

    for i in ans:
        print(" ".join(map(str, i)))

climb_stairs_two(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733753/problem/B
# 🚩 use python3 instead of pypy
