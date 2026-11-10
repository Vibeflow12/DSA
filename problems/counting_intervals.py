n = int(input())

def counting_intervals(t, l, r):
    if l > r:
        return 0

    if t == 1:
        return max(0,r - l - 1)
    elif t == 2:
        return r - l
    elif t == 3:
        return r - l
    elif t == 4:
        return r - l + 1

for _ in range(n):
    t, l, r = map(int, input().split())
    print(counting_intervals(t, l, r))

# https://codeforces.com/group/8gHlHZUflM/contest/725606/my
