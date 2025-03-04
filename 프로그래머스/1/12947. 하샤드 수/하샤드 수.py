def solution(x):
    answer = True
    
    value = 0
    a = x
    n = len(str(a))
    
    for i in range(n):
        value+=(a%10)
        a //= 10
    
    return True if x%value==0 else False