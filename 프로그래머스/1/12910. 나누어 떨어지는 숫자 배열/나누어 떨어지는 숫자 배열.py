def solution(arr, divisor):
    answer = []
    
    q = arr
    while len(q) > 0:
        n = q.pop()
        if n % divisor == 0:
            answer.append(n)
            
    if len(answer) == 0:
        return [-1]
    
    return sorted(answer)