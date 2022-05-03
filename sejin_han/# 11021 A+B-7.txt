# 11021 A+B-7
t = int(input())
x = []
for i in range(1,t+1):
    a, b = map(int, input().split())
    x.append(a+b)
for i in range(t):
    print(f'Case #{i+1}:',x[i])