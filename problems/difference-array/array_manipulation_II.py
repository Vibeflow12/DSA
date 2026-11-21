n, q = map(int, input().split())
arr =list(map(int, input().split()))
arr2 = [0] * (n+1)

def array_manipulation_2(n, q, arr):
    for i in range(q):
        l, r, x = map(int, input().split())
        arr2[l - 1] += x
        arr2[r] -= x

    curr_sum = 0
    max_no = 0

    for i in range(n):
        curr_sum += arr2[i]
        actual_value = arr[i] + curr_sum
        max_no = max(max_no, actual_value)

    print(max_no)

array_manipulation_2(n, q, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/726822/problem/B
# TIME COMPLEXITY
# O(N+Q)
#
# SPACE COMPLEXITY
# O(N)

# difference array technique
