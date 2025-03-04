def solution(x):
    answer = True
    
    value = 0
    a = x
    n = len(str(a))
    
    for i in range(n):
        value+=(a%10)
        a //= 10
    
    if x%value == 0:
        return True
    else:
        return False