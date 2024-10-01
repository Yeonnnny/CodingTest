K = int(input())
stack=[]

for i in range (K):
    num = int(input())  # 돈 입력
    if num==0:          # 잘못된 수 부름
        stack.pop()     # 가장 최근 값 제거
    else: 
        stack.append(num) # 옳은 값 넣기

print(sum(stack)) 
