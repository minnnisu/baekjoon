### 더 나은 방식(테스트 통과 완료)

from collections import deque

def bfs(x, y):
    # 상하좌우 이동 값
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while (len(queue) > 0):
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if(-1 < nx < N and -1 < ny < M and graph[nx][ny] == 1):
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

N, M = map(int, input().split(" "))

graph = []
for i in range(N):
    row_str = input()
    row = [int(i) for i in row_str]
    graph.append(row)

bfs(0, 0)

print(graph[N-1][M-1])


### 내가 처음 푼 방식(테스트 통과 완료)

# from collections import deque

# graph = []

# def bfs(x, y, count, queue):
#     if(x < 0 or y < 0 or x >= N or y >= M):
#         return
    
#     current_node = x * M + (y + 1)
#     if(graph[x][y] != 0):
#         queue.append([current_node, count + 1])
#         graph[x][y] = 0

        

# def init(x, y, count):
#     current_node = x * M + (y + 1)
#     queue = deque([[current_node, count]])
#     graph[x][y] = 0
    
#     while len(queue) > 0:
#         poded_node = queue.popleft()
#         if(poded_node[0] == N * M):
#             print(poded_node[1])
#             return

#         x = (poded_node[0] - 1) // M
#         y = (poded_node[0] - 1) % M

#         bfs(x + 1, y, poded_node[1], queue)
#         bfs(x - 1, y, poded_node[1], queue)
#         bfs(x, y + 1, poded_node[1], queue)
#         bfs(x, y - 1, poded_node[1], queue)
        
#         count += 1

    

# N, M = map(int, input().split(" "))

# for i in range(N):
#     row_str = input()
#     row = [int(i) for i in row_str]
#     graph.append(row)

# init(0, 0, 1)