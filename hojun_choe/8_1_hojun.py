n = [3, 5, 7]
for i in range(8, 1000):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        pass
    else:
        n.append(i)
k = int(input())
x = list(map(int, input().split()))
num = 0
for i in x:
    if i in n:
        num = num + 1
print(num)
