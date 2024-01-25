from itertools import permutations

def solution(babbling):
    answer = 0
    li = ["aya", "ye", "woo", "ma"] # [2,3](1), [4,6](2), [6,9](3), [9,12](4), [10,15]
    
    for i in babbling:        
        if len(i) <=1:
            continue
        elif len(i)<=3:
            if i in li:
                answer+=1
                continue
        else: # 원소 길이 4 이상
            num = (len(i) // 3) if (len(i)%3==0) else (len(i) // 3)+1
            for permut in permutations(li,num):
                if i == "".join(list(permut)):
                    answer+=1
                    
    return answer