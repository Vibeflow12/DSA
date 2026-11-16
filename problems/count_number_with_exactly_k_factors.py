import math

n, q, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_arr = [0] * n

def factors_count(num):
    ans = 0
    s = math.isqrt(num)

    for i in range(1, s + 1):
        if num % i == 0:
            if i * i == num:
                ans += 1
            else:
                ans += 2
    return ans

def count_number_with_exactly_k_factors():
    count = 0

    if factors_count(arr[0]) == k:
        count += 1
    else:
        count += 0
    prefix_arr[0] = count

    for i in range(1, n):
        count = 0

        if factors_count(arr[i]) == k:
            count += 1
        else:
            count += 0
        prefix_arr[i] = count

        prefix_arr[i] = prefix_arr[i - 1] + count

    for i in range(q):
        l, r = map(int, input().split())
        if l == 1:
            ans = prefix_arr[r - 1]
        else:
            ans = prefix_arr[r - 1] - prefix_arr[l - 2]
        print(ans)

count_number_with_exactly_k_factors()

# https://codeforces.com/group/DNruwPkRNA/contest/726133/problem/F
# TIME COMPLEXITY
#
# Factor counting: O(√A) per element.
# Processing all N elements: O(N√A).
# Building prefix array - O(N)
# Processing queries: O(Q), because each query takes O(1).
#
# OVERALL TIME COMPLEXITY
# O(N√A+Q).
#
# SPACE COMPLEXITY
#
# arr - O(n)
# prefic_arr - O(n)
# Temporary variables (l, r, ans): O(1)
#
# OVERALL SPACE COMPLEXITY
# O(n)
