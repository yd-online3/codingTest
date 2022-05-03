# 2439 별 찍기 - 2
a = int(input())
x = '*'
y = ' '
for i in range(a):
    print(f'{y*(a-(i+1))}{x*(i+1)}')