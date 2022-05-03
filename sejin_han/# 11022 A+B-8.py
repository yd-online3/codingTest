# 11022 A+B-8
t = int(input())
x=[]
y=[]
z=[]
for i in range(1,t+1):
    a, b = map(int, input().split())
    x.append(a+b)
    y.append(a)
    z.append(b)
for i in range(t):
    print(f'Case #{i+1}: {y[i]} + {z[i]} = {x[i]}')