def solution(s):
    # 부호 판별: 음수이면 첫 문자가 '-', 양수이면 '+' 또는 숫자
    is_negative = s[0] == '-'
    # 부호 기호가 있으면 제외한 숫자 부분만 사용
    digits = s[1:] if is_negative or s[0] == '+' else s

    answer = 0
    power = 1  # 10의 거듭제곱을 누적할 변수

    # 문자열의 마지막 문자부터 순회
    for ch in reversed(digits):
        answer += int(ch) * power
        power *= 10

    return -answer if is_negative else answer
