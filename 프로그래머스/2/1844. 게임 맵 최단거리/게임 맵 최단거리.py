from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([(0, 0, 1)]) # x, y, 거리
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0:
        return -1
    
    while queue:
        x, y, dist = queue.popleft();
        if x == n-1 and y== m-1:
            return dist
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] ==1 :
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))
    
    return -1