# 정렬 이후 : 자기 자신의 인덱스 = 자기 자신의 값-1

# 정렬 이후 : 자기 자신의 인덱스+1 = 자기 자신의 값

def solution(citations):
    answer = 0
    # 1. 내림차순 정렬 (선택정렬)
    citations.sort(reverse=True)
    
    # 2. value < index+1
    for idx, citation in enumerate(citations):
        if citation < idx+1:
            return idx
    
    return len(citations)
