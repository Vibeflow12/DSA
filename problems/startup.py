import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    brand_cost = [0] * (k + 1)
    for j in range(k):
        bidx, c = map(int, input().split())
        brand_cost[bidx] += c

    sorted_amount = sorted(brand_cost[1:], reverse=True)
    total_amount = sum(sorted_amount[:n])
    print(total_amount)

# https://codeforces.com/problemset/problem/2036/B

# Time Complexity
#
# Initialize the list
#brand_cost = [0] * (k + 1) - O(k)
#
# Aggregate bottle costs
# for j in range(k):
    # bidx, c = map(int, input().split())
    # brand_cost[bidx] += c  - O(k)
    #
# Sorting
#sorted_amount = sorted(brand_cost[1:], reverse=True) - O(k log k)
#
# summation
# total_amount = sum(sorted_amount[:n]) -O(min(n,k)) - O(n)
#
# OVERALL T.C
#
# O(k) + O(k) + O(k log k) + O(n)
#
#Space Complexity
#
# brand_cost - O(k) 
# sorted_amount - O(k) 
# sorted_amount[:n] - O(n) 
# 
# OVERALL S.C
# 
# O(k)
