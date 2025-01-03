num = int(input())

d = [0 for _ in range(31)]

def dp(x):
    if x == 0 : return 1
    if x == 1 : return 0
    if x == 2 : return 3
    if d[x] != 0 : return d[x]
    
    result = dp(x-2)*3
    for i in range(3, x+1):
        if i%2==0 :
            result+=2*dp(x-i)
            
    d[x] = result
    return d[x]

print(dp(num))
