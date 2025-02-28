def solution(n):
    answer = ""
    
    l = [s for s in str(n)]
    l.sort(reverse=True)
    
    for i in l:
        answer += i
    
    return int(answer)