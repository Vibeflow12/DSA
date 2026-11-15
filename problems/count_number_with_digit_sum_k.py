n, q, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_arr = [0] * n

def count_number_with_digit_sum_k():
    temp = arr[0]
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp = temp // 10

    if digit_sum == k:
        prefix_arr[0] += 1
    else:
        prefix_arr[0] += 0

    for i in range(1, n):
        temp = arr[i]
        digit_sum = 0

        while temp > 0:
            digit_sum += temp % 10
            temp = temp // 10

        if digit_sum == k:
            prefix_arr[i] += 1
        else:
            prefix_arr[i] += 0

        prefix_arr[i] = prefix_arr[i - 1] + prefix_arr[i]

    for i in range(q):
        l, r = map(int, input().split())
        if l == 1:
            ans = prefix_arr[r - 1]
        else:
            ans = prefix_arr[r - 1] - prefix_arr[l - 2]
        print(ans)

count_number_with_digit_sum_k()

#https://codeforces.com/group/DNruwPkRNA/contest/726133/problem/E
#
# TIME COMPLEXITY
#
# First element's digit sum - O(D)
# Building prefix array - O(N × D), because you calculate the digit sum of every element
# Processing queries: O(Q), because each query takes O(1).
#
# OVERALL TIME COMPLEXITY
# O(N × D + Q)
#
# SPACE COMPLEXITY
#
# arr - O(n)
# prefic_arr - O(n)
# Temporary variables (temp, digit_sum, l, r, ans): O(1)
#
# OVERALL SPACE COMPLEXITY
# O(n)
