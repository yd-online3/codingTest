# 10950 A+B - 3
t = int(input())
x = []
for i in range(t):
    a, b = map(int, input().split())
    x.append(a+b)
for i in range(t):
    print(x[i])