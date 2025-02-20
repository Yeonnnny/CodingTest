# def solution(n):
#     answer = []
    
#     while n > 0:
#         answer.append(n%10)
#         n //= 10
    
#     return answer


def solution(n):
    return list(map(int, reversed(str(n))))