n=int(input())
a=list(map(int,input().split()))

def sum_of_all_subarrays(n,a):
    for i in range(0,n):
        for j in range(i,n):
            count = 0
            for k in range(i,j+1):
                count += a[k]
            print(count)

sum_of_all_subarrays(n, a)

# https://codeforces.com/group/DNruwPkRNA/contest/726083/problem/B
