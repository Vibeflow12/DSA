n, q = map(int, input().split())
arr = [0] * (n + 1)

def array_manipulation(n, q, arr):
    for i in range(q):
        l, r, x = map(int, input().split())
        arr[l - 1] += x
        arr[r] -= x

    curr_sum = 0
    max_no = 0

    for i in range(n):
        curr_sum += arr[i]
        max_no = max(max_no, curr_sum)

    print(max_no)

array_manipulation(n, q, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/726822/problem/A

# TIME COMPLEXITY
# O(N+Q)
#
# SPACE COMPLEXITY
# O(N)
