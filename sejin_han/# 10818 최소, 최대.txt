# 10818 최소, 최대
N = int(input())
a = list(map(int, input().split()))
m = 1000000
M = -1000000
for i in range(N):
    if a[i] <= m:
        m = a[i]
    if a[i] >= M:
        M = a[i]
print(m,M)