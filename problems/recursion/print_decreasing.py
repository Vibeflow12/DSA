import sys
sys.setrecursionlimit(20000)

n = int(input())

def decreasing(num):
    if num == 0:
        return
    print(num)
    return decreasing(num - 1)

def print_decreasing(n):
    decreasing(n)

print_decreasing(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/A
#
# 🚩 use python3 instead of pypy
#
# TIME COMPLEXITY AND SPACE COMPLEXITY
#
# Time: O(N) — one function call per number.
# Space: O(N) — recursive call stack.
