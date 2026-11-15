n,q=map(int,input().split())
arr=list(map(int,input().split()))

prefix_arr= [0] * n

def range_sum_of_squares():
    prefix_arr[0] = arr[0] ** 2

    for i in range(1,n):
        prefix_arr[i] = prefix_arr[i- 1] + (arr[i]  ** 2 )

    print(prefix_arr)

    for i in range(q):
        l,r=map(int,input().split())
        if l==1:
            ans = prefix_arr[r-1]
        else:
            ans = prefix_arr[r-1] - prefix_arr[l-2]
        print(ans)

range_sum_of_squares()

# https://codeforces.com/group/DNruwPkRNA/contest/726133/problem/D
#
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
#
# OVERALL space COMPLEXITY
# O(n)
