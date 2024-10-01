import itertools

n = int(input())    # 총 카드의 수
k = int(input())    # 선택할 카드의 수
cards=[]            # 카드 번호 저장할 리스트
result = []         # 조합을 저장할 리스트


for i in range(n):  # 카드 번호 입력받기
    cards.append(input())

# for permutated in itertools.permutations(cards,k):
#     val = ""
#     for p in permutated:
#         val+=p
#     result.append(val)
for permutated in itertools.permutations(cards,k):
    result.append("".join(permutated))

print(len(set(result)))