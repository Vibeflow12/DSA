import math

n = int(input())
factors = []
second = []

s = int(math.sqrt(n))
for i in range(1, s + 1):
    if n % i == 0:
        factors.append(i)

        if i != n // i:
            second.append(n // i)

print(*(factors + second[::-1]))

# https://codeforces.com/group/8gHlHZUflM/contest/725606/problem/G
