a, b = input().split()
a = int(a)
b = int(b)
for i in range(a, b+1):
    check = True
    if i > 1:
        for j in range(2, int(i**0.5)+1):
            if i % j ==0:
                check = False
                break
        if check:
            print(i)
