from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    # 한 글자 차이나는지 여부
    def is_one_letter_diff(w1, w2):
        diff_count = sum(1 for a, b in zip(w1, w2) if a!=b)
        return diff_count == 1
    
    # BFS
    queue = deque([(begin, 0)])
    v = set()
    
    while queue:
        current, steps = queue.popleft()
        if current == target :
            return steps
        for word in words:
            if word not in v and is_one_letter_diff(current, word):
                v.add(word)
                queue.append((word, steps+1))
    return 0
    
    answer = 0
    return answer