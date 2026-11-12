n=int(input())
a=list(map(int,input().split()))

def sum_of_all_subarrays(n,a):
    for i in range(0,n):
        count = 0
        for j in range(i,n):
                count += a[j]
                print(count)

sum_of_all_subarrays(n, a)

# https://codeforces.com/group/DNruwPkRNA/contest/726083/problem/C
