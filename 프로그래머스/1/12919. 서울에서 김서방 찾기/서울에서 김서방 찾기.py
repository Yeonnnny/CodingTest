def solution(seoul):
    answer = ''
    
    # for i, name in enumerate(seoul):
    #     if name == "Kim":
    #         answer = f'김서방은 {i}에 있다'
    # return answer
    return "김서방은 {}에 있다".format(seoul.index("Kim"))