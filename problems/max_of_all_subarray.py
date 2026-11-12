n=int(input())
a=list(map(int,input().split()))

def max_of_all_subarrays(n,a):
    for i in range(0,n):
        count = a[i]
        for j in range(i,n):
                count = max(count,a[j])
                print(count)

max_of_all_subarrays(n, a)

# https://codeforces.com/group/DNruwPkRNA/contest/726083/problem/D
