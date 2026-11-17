import sys

sys.setrecursionlimit(200000)

n = int(input())

def som_of_natural_numbers(num):
    if num == 0:
        return 0
    smallno = som_of_natural_numbers(num - 1)
    ans = num + smallno
    return ans

def sum_0f_first_n_natural_numbers(n):
    print(som_of_natural_numbers(n))

sum_0f_first_n_natural_numbers(n)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/F
# 🚩 use python3 instead of pypy
