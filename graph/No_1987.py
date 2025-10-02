### 이전 풀이

# import sys
# input = sys.stdin.readline

# R, C = map(int, input().split(" "))

# graph = []
# for _ in range(R):
#     graph.append(list(input().strip()))

# answer = 0
# count = 0
# visited = [False] * 26
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]


# def dfs(x, y):
#     global count
#     visited[ord(graph[x][y]) - 65] = True
#     count += 1

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if(0 <= nx < R and 0 <= ny < C):
#             if(visited[ord(graph[nx][ny]) - 65] == False):
#                 dfs(nx, ny)
#     global answer         
#     answer = max(answer, count)

#     visited[ord(graph[x][y]) - 65] = False
#     count -= 1

# dfs(0, 0)
# print(answer)


### 더 나은 풀이
import sys
input = sys.stdin.readline

R, C = map(int, input().split(" "))
graph = []
answer = 0
visited = [False] * 26
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(R):
    graph.append(list(input().strip()))

def dfs(x, y, cnt):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if(0 <= nx < R and 0 <= ny < C):
            n = ord(graph[nx][ny]) - 65
            if(visited[n] == False):
                visited[n] = True
                dfs(nx, ny, cnt + 1)
                visited[n] = False

    global answer         
    answer = max(answer, cnt)


visited[ord(graph[0][0]) - 65] = True
dfs(0, 0, 1)
print(answer)