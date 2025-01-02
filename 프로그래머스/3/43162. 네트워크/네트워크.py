# dfs
def solution(n, computers):

    def dfs(idx):
        visited[idx] = 1
        for i in range(len(computers[idx])):
            if computers[idx][i] and not visited[i]:
                dfs(i)

    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1

    return answer
