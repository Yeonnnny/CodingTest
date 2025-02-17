def solution(n):
    answer = n
    
    m=n//2
    
    while m>0:
        if n%m==0:
            answer+=m
        m-=1
    
    
    return answer