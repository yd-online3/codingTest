import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
if n == 1:
    print(a[0])
    print(a[0])
    print(a[0])
    print(0)
else:
    print(round(sum(a)/n))
    print(a[n//2])
    num = []
    b = a.copy() # -2 -1 -3 -1 -2
    for i in list(set(b)): # 중복 제거
        num.append([b.count(i), i]) # [빈도수, 숫자] : [[1, -3], [2, -1],  [2, -2]]
        b.remove(i)         

    num.sort(key=lambda x:x[0]) # 빈도수로 정렬 [[1, -3], [2, -2], [2, -1]]

    if num[0][0] == num[-1][0]: # 모든수의 빈도수가 동일 할때
        num.sort(key=lambda x:x[1]) # 숫자로 정렬
        print(num[1][1])
    elif num[-1][0] == num[-2][0]: # 최빈값 여러개 끝에서 2번째
        print(num[-2][1])
    else:
        print(num[-1][1])
        
    print(a[-1] - a[0])
