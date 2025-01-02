def solution(numbers, target):
    answer = 0
    
    def dfs(index, current_sum):
        if index == len(numbers): # 끝까지 탐색한 경우
            return 1 if current_sum==target else 0 # 타겟과 현재까지 합 일치하면 1 반환
        # 현재 숫자를 더하는 경우, 빼는 경우 구하기 
        return dfs(index+1, current_sum+numbers[index]) + dfs(index+1, current_sum-numbers[index])
    
    return dfs(0,0)