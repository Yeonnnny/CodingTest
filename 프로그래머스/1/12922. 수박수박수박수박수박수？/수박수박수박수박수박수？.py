def solution(n):
    s = '수'
    b = '박'
    
    if n%2==0:
        return (s+b)*(n//2)
    return (s+b)*(n//2) + s