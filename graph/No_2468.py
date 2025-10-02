from collections import deque

N = int(input())
answer = 0

maxHeight = 0

graph = []
for i in range(N):
    graph.append(list(map(int,input().split(" "))))
    for j in range(N):
        if(graph[i][j] > maxHeight):
            maxHeight = graph[i][j]


def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(queue) > 0:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < N and 0 <= ny < N):
                if(visited[nx][ny] == False):
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    
    
for i in range(maxHeight):
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0

    for j in range(N):
        for k in range(N):
            if(graph[j][k] <= i):
                visited[j][k] = True
    
    for x in range(N):
        for y in range(N):
            if(visited[x][y] == False):
                bfs(x, y, visited)
                count += 1
    answer = max(answer, count)          

print(answer)