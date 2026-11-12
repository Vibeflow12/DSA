n=int(input())
a=list(map(int,input().split()))

for i in range(0,n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(a[k],end=" ")
        print()

# https://codeforces.com/group/DNruwPkRNA/contest/726083/problem/A
