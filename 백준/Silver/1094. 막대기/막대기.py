# 1. while (total>X) :  -> 스택 push/pop & total 값 갱신
# 2. total == X : 스택의 크기 반환


# X 값 입력 받음
X = int(input())

total=64    # 남은 막대기 길이 총합
stack=[64]  # 남은 막대기 저장할 스택


while total > X:
    top = stack.pop()   # 가장 나중에 들어간 값 꺼내기
    num = top//2        # 절반으로 자르기
    stack.append(num)   # 잘라서 한쪽 절반을 스택에 추가
    
    if total - num >= X:
        total -= num    # 나머지 버리기
    else:
        stack.append(num)   # 나머지 버리지 않음
        # total = sum(stack)
#     print( "total : ",total)
    
# print("최종 stack : ", stack)
print(len(stack))
    