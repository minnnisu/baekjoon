from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
N, M = map(int, input().split(" "))
answer = 0

def bfs():
    queue = deque([])
    tmp_graph = deepcopy(graph)
  

    # 바이러스 삽입
    for i in range(N):
        for j in range(M):
            if(tmp_graph[i][j] == 2):
                queue.append((i, j))
    

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if(0 <= nx < N and 0 <= ny < M):
                if(tmp_graph[nx][ny] == 0):
                    tmp_graph[nx][ny] = 2
                    queue.append((nx, ny))

    
    cnt = 0
    for i in range(N):
        cnt += tmp_graph[i].count(0)

    global answer
    answer = max(answer, cnt)

def backtrack(n):
    if(n == 3):
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if(graph[i][j] == 0):
                graph[i][j] = 1
                backtrack(n + 1)
                graph[i][j] = 0

for i in range(N):
    graph.append(list(map(int, input().split(" "))))

backtrack(0)
print(answer)