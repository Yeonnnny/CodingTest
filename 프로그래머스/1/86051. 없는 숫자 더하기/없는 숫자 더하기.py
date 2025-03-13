def solution(numbers):
    total = [i for i in range(10)]
    return sum(list(set(total)-set(numbers)))