def solution(n):
    answer = 0
    
    if n == int(n**(1/2))**2:
        answer = (n**(1/2)+1)**2
    else:
        answer = -1
    
    return answer