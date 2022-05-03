# 2525 오븐 시계
h, m = map(int, input().split())
t = int(input())
if m+t >= 60:
    a = int((m+t)/60)
    b = (m+t)%60
    if h+a >= 24:
        print((h+a)%24,b)
    else:
        print((h+a),b)
else:
    print(h,(m+t))