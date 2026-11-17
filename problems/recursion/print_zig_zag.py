import sys
sys.setrecursionlimit(20000)

n = int(input())

def zig_zag(num):

    if num == 0:
        return
    print(num)
    if num == 1:
        return
    zig_zag(num - 1)
    print(num)

def print_zig_zag(n):
    zig_zag(n)

print_zig_zag(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/C
#
# 🚩 use python3 instead of pypy
#
# TIME COMPLEXITY AND SPACE COMPLEXITY
#
# Time: O(N) — one function call per number.
# Space: O(N) — recursive call stack.
