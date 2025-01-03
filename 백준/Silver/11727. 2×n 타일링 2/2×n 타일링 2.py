num = int(input())


b = [0 for _ in range(1001)]

def dp(x):
    if x == 1 : return 1
    if x == 2 : return 3
    if b[x] != 0 : return b[x]
    b[x] = dp(x-2)*2 + dp(x-1)
    return b[x]%10007

print(dp(num))