import sys
input =sys.stdin.readline

n = int(input()) # 개수

num=[]
dic = dict()
num_sum = 0


for i in range(n):
    number = int(input())
    num.append(number)

    num_sum+=number

    # 코드 참고
    if number not in dic:
        dic[number]=1
    else:
        dic[number]+=1
    
num.sort() # 리스트 정렬 (2,3번에서 필요)

mean = round(num_sum/n) # 평균
median = num[(n//2)] # 중앙값
range = num[-1]-num[0] # 범위


# 최빈값
# 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 코드 참고

max_count = max(dic.values()) # 최빈 개수

numbers = []
for i in sorted(set(num)):
    if dic[i] == max_count:
        numbers.append(i)

if len(numbers)==1:
    mode = numbers[0]
else:
    numbers.sort()
    mode=numbers[1]


print(mean)
print(median)
print(mode)
print(range)

