n = int(input())
a = list(map(int, input().split()))

def sum_of_all_subarrays(n, a):
    sum = 0
    for i in range(0, n):
        sum += a[i] * (n - i) * (i + 1)
    print(sum)

sum_of_all_subarrays(n, a)

# https://codeforces.com/group/DNruwPkRNA/contest/726083/problem/G
