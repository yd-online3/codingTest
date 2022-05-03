# 2562 최댓값
a = []
for i in range(9):
    a.append(int(input()))
M = a[0]
x = 1
for i in range(9):
    if a[i] >= M:
        M = a[i]
        x = i+1
print(M)
print(x)