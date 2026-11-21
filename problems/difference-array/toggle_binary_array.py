n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [0] * (n + 1)

def toggle_binary_array(n, q, arr):
    for i in range(q):
        l, r = map(int, input().split())
        arr2[l - 1] ^= 1
        arr2[r] ^= 1

    toggle = 0

    for i in range(n):
        toggle ^= arr2[i]

        arr[i] ^= toggle

    print(" ".join(map(str, arr)))

toggle_binary_array(n, q, arr)

# https://codeforces.com/group/DNruwPkRNA/contest/726822/problem/C
# TIME COMPLEXITY
# O(N+Q)
#
# SPACE COMPLEXITY
# O(N)

# difference array technique
