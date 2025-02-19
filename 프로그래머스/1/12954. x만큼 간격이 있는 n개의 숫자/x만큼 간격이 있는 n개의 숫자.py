def solution(x, n):
    answer = []
    
    answer.append(x)
    num = x
    
    for i in range(n-1):
        x+=num
        answer.append(x)
        
    
    return answer