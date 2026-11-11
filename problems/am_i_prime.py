import math

n = int(input())

def am_i_prime(n):
    s=int(math.sqrt(n))
    if n<= 1:
        return "NO"
    for i in range(2,s+1):
        if n % i ==0:
            return "NO"

    return "YES"

print(am_i_prime(n))

# https://codeforces.com/group/8gHlHZUflM/contest/725606/problem/E
