# 2480 주사위 세개
a, b, c = map(int, input().split())
if (a == b) & (b == c):
    print(10000+(1000*a))
elif (a != b) & (b != c) & (c != a):
    if(a >= b) & (a >= c):
        print((100*a))
    elif(b >= c) & (b >= a):
        print((100*b))
    else:
        print((100*c))
else:
    if(a == b):
        print((100*a)+1000)
    elif(b == c):
        print((100*b)+1000)
    else:
        print((100*c)+1000)