import math

n = int(input())

def count_factors(n):
    count = 0
    s = int(math.sqrt(n))
    for i in range(1, s + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2

    return count

print(count_factors(n))

# https://codeforces.com/group/8gHlHZUflM/contest/725606/problem/D
