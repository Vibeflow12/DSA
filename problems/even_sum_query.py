n = int(input())
arr = list(map(int, input().split()))
w = int(input())

prefix_arr = [0] * n

def even_sum_querys():
    prefix_arr[0] = 0

    for i in range(1, n):
        if i % 2 != 0:
            prefix_arr[i] = prefix_arr[i - 1] + arr[i]
        else:
            prefix_arr[i] = prefix_arr[i - 1]

    for i in range(w):
        l, r = map(int, input().split())
        if l == 1:
            ans = prefix_arr[r - 1]
        else:
            ans = prefix_arr[r - 1] - prefix_arr[l - 2]
        print(ans)

even_sum_querys()

# https://codeforces.com/group/DNruwPkRNA/contest/726133/problem/B#
#
# TIME COMPLEXITY
# Initialize prefix array
# prefix_arr = [0] * n  - O(n)
#
# Initialize first prefix value
#   prefix_arr[0] = arr[0] - O(1)
#
# Build prefix array
#  for i in range(1, n):
    # if arr[i] % 2 ==0:
    #     prefix_arr[i] = prefix_arr[i - 1] + arr[i]
    # else:
    #     prefix_arr[i] = prefix_arr [i-1] - O(n)
#
# process queries
# for i in range(w): - O(n)
#
# Calculate each query
#  prefix_arr[i] = prefix_arr[i - 1] + arr[i]  O(1)
#
# OVERALL TIME COMPLEXITY
#
# O(n) + O(n) + O(w)
# O(n+w)
#
# SPACE COMPLEXITY
#
# arr - O(n)
# prefic_arr - O(n)
# query var l,r,ans - O(1)
#
# OVERALL SPACE COMPLEXITY
# O(n)
#
