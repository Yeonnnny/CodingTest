def solution(k, m, score):
    answer = 0
    s_len = len(score)
    score.sort(reverse=True)
    return sum([score[i]*m for i in range(s_len) if (i+1)%m == 0 ])