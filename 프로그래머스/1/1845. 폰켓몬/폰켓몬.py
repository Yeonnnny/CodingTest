def solution(nums):
    max = len(nums)//2
    answer = len(set(nums)) if len(set(nums))< max else max
    return answer