import bisect
n,q = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
for i in range(q):
    x = int(input())
    print(n-bisect.bisect_left(a,x))

