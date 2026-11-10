n = int(input())

def interval_sum(l, r):
    R = r * (r + 1) // 2
    L = l * (l - 1) // 2
    return R - L

for _ in range(n):
    l, r = map(int, input().split())
    print(interval_sum(l, r))

# https://codeforces.com/group/8gHlHZUflM/contest/725606/submit
