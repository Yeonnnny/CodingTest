from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # 한 글자만 다른지 여부
    def is_one_letter_diff(w1,w2):
        diff_count = 0
        for a,b in zip(w1,w2):
            if a!=b:
                diff_count+=1
        return 1 if diff_count == 1 else 0
    
    queue = deque([(begin, 0)])
    v = [0]*len(words)

    # BFS 탐색
    while queue:
        current, steps = queue.popleft()

        if current == target :
            return steps
        
        for i, word in enumerate(words):
            if not v[i] and is_one_letter_diff(current,word):
                v[i] = 1
                queue.append((word, steps+1))


    return 0