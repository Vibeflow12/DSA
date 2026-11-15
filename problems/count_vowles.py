n = int(input())
arr = list(input().strip())
q = int(input())

prefix_arr = [0] * n

def count_vowles():
    vowles = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if arr[0] in vowles:
        prefix_arr[0] = 1
    else:
        prefix_arr[0] = 0

    for i in range(1, n):
        if arr[i] in vowles:
            prefix_arr[i] = prefix_arr[i - 1] + 1
        else:
            prefix_arr[i] = prefix_arr[i - 1]

    for i in range(q):
        l, r = map(int, input().split())
        if l == 1:
            ans = prefix_arr[r - 1]
        else:
            ans = prefix_arr[r - 1] - prefix_arr[l - 2]

        print(ans)

count_vowles()

# https://codeforces.com/group/DNruwPkRNA/contest/726133/problem/C

# TIME COMPLEXITY
#
# Read input	            - O(n)
# Initialize prefix array	- O(n)
# Build prefix array	    - O(n)
# Process one query	        - O(1)
# Process q queries	        - O(q)
#
# OVERALL TIME COMPLEXITY
# O(n + q)
#
# SPCAE COMPLEXITY
#
# arr	            - O(n)
# prefix_arr	    - O(n)
# vowels	        - O(1)
# Other variables	- O(1)
#
# OVERALL space COMPLEXITY
# O(n)
