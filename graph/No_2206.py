from collections import deque

N, M = map(int, input().split(" "))
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    graph.append(list(map(int, input().strip())))

move = [[[0, 0] for _ in range(M)] for _ in range(N)]

def bfs():
    q = deque([])
    q.append((0, 0, 0))
    move[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if(x == N - 1 and y == M - 1):
            print(move[x][y][z])
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < N and 0 <= ny < M):
                if(graph[nx][ny] == 1 and z == 0):
                    move[nx][ny][1] = move[x][y][0] + 1
                    q.append((nx, ny, 1))
                
                if(graph[nx][ny] == 0 and move[nx][ny][z] == 0):
                    move[nx][ny][z] = move[x][y][z] + 1
                    q.append((nx, ny, z))
    print(-1)

bfs()