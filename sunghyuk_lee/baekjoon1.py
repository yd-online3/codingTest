# 1단계

# 1번
print('Hello World!')

# 2번
print('강한친구 대한육군', '강한친구 대한육군', sep='\n')

# 3번
print('\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \(__)|')

# 4번

A, B = map(int, input().split())
print(A+B)

# 5번

A, B = map(int, input().split())
print(A+B)

# 6번

A, B = map(int, input().split())
print(A-B)

# 7번

A, B = map(int, input().split())
print(A*B)

# 8번

A, B = map(int, input().split())
print(A/B)

# 9번

A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)

# 10번

id = input('')
print(f'{id}??!')

# 11번

bool = int(input())
print(bool-543)

# 12번

A, B, C = map(int, input().split())

print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep="\n")

# 13번

A = int(input())
B = str(input())

B1 = int(B[2])
B2 = int(B[1])
B3 = int(B[0])
B = int(B)

print(A*B1,A*B2,A*B3,A*B,sep='\n')


# 2단계

# 1번

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

# 2번

a = int(input())

if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')

# 3번

a = int(input())

if a % 4 == 0 and (a % 100 !=0 or a % 400 == 0):
    print(1)
else:
    print(0)

# 4번

x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)

# 5번

h, m = map(int, input().split())

if m>=45:
    print(h, m-45)
else:
    if h==0:
        print(23, 15+m)
    else:
        print(h-1, 15+m)

# 6번

h, m = map(int, input().split())
c = int(input())

if (m+c) // 60 >= 1:
    if h+((m+c)//60) >= 24:
        print(h+((m+c)//60)-24, (m+c) % 60)
    else:
        print(h+((m+c)//60), (m+c) % 60)
else:
    print(h, m+c)


# 3단계

# 1번

x = int(input())

for i in range(1,10):
    print(f'{x} * {i} = {x * i}')

# 2번

x = int(input())

for i in range(x):
    A, B = map(int, input().split())
    print(A+B)

# 3번

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# 4번

import sys
T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

# 5번

import sys
T = int(input())

for i in range(1, T+1):
    print(i)

# 6번

a = int(input())

for i in range(a):
    print(a-i)

# 7번

T = int(input())

for i in range(1,T+1):
    A, B = map(int, input().split())
    print(f'Case #{i}: {A+B}')

# 8번

T = int(input())

for i in range(1,T+1):
    A, B = map(int, input().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')

# 9번

T = int(input())

for i in range(1,T+1):
    print('*' * i)

# 10번

T = int(input())

for i in range(1,T+1):
    print(f'{"*" * i:>{T}}')

# 11번

n, x = map(int,input().split())
num = list(map(int,input().split()))
for i in range(n):
    if num[i] < x:
        print(num[i], end = ' ')

# 12번

while True:
    A, B = map(int, input().split())
    if A+B != 0:
        print(A+B)
    else:
        break

# 13번

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

# 14번

input_num = int(input())

num = input_num  
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  
    new_num = ((num % 10) * 10) + (sum_num % 10)  
    cnt += 1  
    if new_num == input_num :
        break
    num = new_num  
print(cnt)

# 4단계

# 1번

input_num = int(input())
num = list(map(int,input().split()))

print(min(num), end=' ')
print(max(num))

# 2번

num_list = []
for i in range(9):
    num_list.append(int(input()))


print(max(num_list))
print(num_list.index(max(num_list))+1)

# 3번

num_list = []
for i in range(10):
    num_list.append(int(input()) % 42)

num_list = set(num_list)
print(len(num_list))

# 4번

n = int(input())
record = list(map(int,input().split()))
new_record = []
for i in range(n):
    new_record.append(record[i] / max(record))
    
sum = 0
for i in range(n):
    sum += new_record[i]

print(sum/ n * 100)

# 5번

n = int(input())
record = list(map(int,input().split()))
new_record = []
for i in range(n):
    new_record.append(record[i] / max(record))
    
sum = 0
for i in range(n):
    sum += new_record[i]

print(sum/ n * 100)

# 6번

n = int(input())

for i in range(n):
    list = list(input())
    score = 0  
    sum = 0  # 
    for j in list:
        if j == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(score)

# 7번

n = int(input())

for _ in range(n):
    num = list(map(int, input().split()))
    average = sum(num[1:])/num[0]  
    count = 0
    for score in num[1:]:
        if score > average:
            count += 1  
    rate = cnt/num[0] *100
    print(f'{rate:.3f}%')

# 5단계

# 1번
def solve(a):
    return sum(a)