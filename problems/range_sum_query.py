n = int(input())
arr = list(map(int, input().split()))
w = int(input())

prefix_arr = [0] * n


def rang_sum_querys():
    prefix_arr[0] = arr[0]

    for i in range(1, n):
        prefix_arr[i] = prefix_arr[i - 1] + arr[i]

    for i in range(w):
        l, r = map(int, input().split())
        if l == 1:
            ans = prefix_arr[r - 1]
        else:
            ans = prefix_arr[r - 1] - prefix_arr[l - 2]
        print(ans)


rang_sum_querys()

# https://codeforces.com/group/DNruwPkRNA/contest/726133/problem/A
#
# TIME COMPLEXITY
# Initialize prefix array
# prefix_arr = [0] * n  - O(n)
#
# Construct prefix sum
# for i in range(1, n):
    # prefix_arr[i] = prefix_arr[i-1] + arr[i]- O(n)
#
# Process queries
# for i in range(w):
    # l, r = map(int, input().split())  - O(w)
#
# OVERALL TIME COMPLEXITY
#
# O(n) + O(n) + O(w)
# O(n+w)
#
# SPACE COMPLEXITY
# arr - O(n)
# prefic_arr - O(n)
# query var l,r,ans - O(1)
#
# OVERALL SPACE COMPLEXITY
# O(n)
#
