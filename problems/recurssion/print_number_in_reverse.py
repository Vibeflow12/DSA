import sys
sys.setrecursionlimit(20000)

n = int(input())

def reverse(num):

    if num == 0:
        return
    print(num%10,end="")
    reverse(num//10)

def print_number_in_reverse(n):
    if n==0:
        print(0)
    reverse(n)

print_number_in_reverse(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/D
#
# 🚩 use python3 instead of pypy
#
# TIME COMPLEXITY AND SPACE COMPLEXITY
#
# Time: O(N) — one function call per number.
# Space: O(N) — recursive call stack.
