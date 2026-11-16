n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefix_arr = [0] * n

def count_number_with_exactly_k_factors():
    prefix_arr[0] = arr[0]

    for i in range(1, n):
        count = 0

        if i % 2 == 0:
            count += arr[i]
        else:
            count -= arr[i]

        prefix_arr[i] = count

        prefix_arr[i] = prefix_arr[i - 1] + count

    for i in range(q):
        l, r = map(int, input().split())

        if l == 1:
            ans = prefix_arr[r - 1]
        else:
            ans = prefix_arr[r - 1] - prefix_arr[l - 2]

        if l % 2 == 0:
            ans *= -1

        print(ans)

count_number_with_exactly_k_factors()

# https://codeforces.com/group/DNruwPkRNA/contest/726133/problem/G
#
# TIME COMPLEXITY
#
# Building the alternating prefix array - O(N)
# Processing each query - O(1)
# Processing all Q queries - O(Q)
#
# OVERALL TIME COMPLEXITY
# O(N+Q).
#
# SPACE COMPLEXITY
#
# arr - O(n)
# prefic_arr - O(n)
# Temporary variables (l, r, ans): O(1)
#
# OVERALL SPACE COMPLEXITY
# O(n)
