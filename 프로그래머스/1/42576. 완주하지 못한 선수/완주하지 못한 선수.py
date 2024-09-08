def solution(participant, completion):
    # 정렬
    participant.sort()
    completion.sort()

    # 두 리스트를 비교하여 불일치 항목 찾기
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    # 모든 항목이 일치한 경우, 마지막 항목이 완료되지 않은 참가자
    return participant[-1]