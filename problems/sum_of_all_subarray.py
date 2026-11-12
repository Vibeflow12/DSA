n=int(input())
a=list(map(int,input().split()))

def sum_of_all_subarrays(n,a):
    total =0
    for i in range(0,n):
        count = 0
        for j in range(i,n):
                count = count + a[j]
                total +=  count
    print(total)

sum_of_all_subarrays(n, a)

# https://codeforces.com/group/DNruwPkRNA/contest/726083/problem/E
