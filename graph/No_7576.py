from collections import deque

def bfs(graph, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    init_tomato_array = []
    total_tomato = N * M
    current_tomato = 0
    day = 0

    for i in range(N):
        for j in range(M):
            if(graph[i][j] == 1):
                init_tomato_array.append((i, j))
                current_tomato += 1
            
            if(graph[i][j]== -1):
                total_tomato -= 1

    queue = deque(init_tomato_array)

    while(len(queue) > 0):
        x, y = queue.popleft()
        day = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < N  and 0 <= ny < M and graph[nx][ny] == 0):
                queue.append((nx, ny))
                graph[nx][ny] = day + 1
                current_tomato += 1

    if(current_tomato == total_tomato):
        return day - 1
    else:
        return -1


M, N = map(int, input().split(" "))

graph = []

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)


print(bfs(graph, N, M))