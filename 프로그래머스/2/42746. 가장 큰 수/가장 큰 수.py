# def solution(numbers):
#     numbers = list(map(str, numbers))
    
#     # 삽입정렬 (내림차순)
#     for i in range(1, len(numbers)):
#         key = numbers[i]
#         j = i-1
        
#         # 현재 값과 이전 값을 비교
#         while j >= 0 and  (key+numbers[j] > numbers[j]+key) :
#             numbers[j+1] = numbers[j]
#             j-=1
        
#         numbers[j+1] = key
        
#     answer = ''.join(numbers)
    
#     return answer if answer[0] != '0' else '0'

def solution(numbers):

    # 숫자를 문자열로 변경
    num = list(map(str, numbers))
    
    # 정렬 기준 : x*3을 사용해 내림차순 정렬
    num = sorted(num, key = lambda x : x*3, reverse= True)
    
    # 모든 숫자가 0인 경우
    if num[0] == '0':
        return '0'
    
    answer = ''.join(num)
    return answer
    