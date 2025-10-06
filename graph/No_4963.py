from collections import deque

w = 0
h = 0
graph = []
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    graph[x][y] = 0

    while q:
        tx, ty = q.popleft()
        
        for i in range(8):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if(0 <= nx < h and 0 <= ny < w):
                if(graph[nx][ny] == 1):
                    q.append((nx, ny))
                    graph[nx][ny] = 0

while True:
    w, h = map(int, input().split(" "))
    if(w == 0 and h == 0):
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split(" "))))
    
    count = 0
    for x in range(h):
        for y in range(w):
            if(graph[x][y] == 1):
                bfs(x, y)
                count += 1
    print(count)