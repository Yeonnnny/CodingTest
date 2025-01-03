# 동적 프로그래밍

num = int(input())

d = [0 for _ in range(1001)]

def dp(x):
    if x==1 : return 1
    if x==2 : return 2
    if d[x] != 0 : return d[x]
    d[x] = dp(x-1) + dp(x-2)
    return d[x] % 10007

print(dp(num))
