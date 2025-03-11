def solution(absolutes, signs):
    # answer = 123456789
    answer = 0
    
    for i,j in zip(absolutes, signs):
        if j :
            answer+= i
        else : 
            answer-=i
    
    return answer