import sys
sys.setrecursionlimit(20000)

n = int(input())

def increasing(num):
    if num == 0:
        return
    increasing(num - 1)
    print(num)

def print_increasing(n):
    increasing(n)

print_increasing(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/B
#
# 🚩 use python3 instead of pypy
#
# TIME COMPLEXITY AND SPACE COMPLEXITY
#
# Time: O(N) — one function call per number.
# Space: O(N) — recursive call stack.
