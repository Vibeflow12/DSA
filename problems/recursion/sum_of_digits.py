import sys

sys.setrecursionlimit(200000)

n = int(input())

def son(n):
    if n == 0:
        return 0
    return n % 10 + son(n // 10)

def sum_of_digits(n):
    print(son(n))

sum_of_digits(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/H
# 🚩 use python3 instead of pypy
