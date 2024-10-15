# from collections import deque

# N = int(input())

# def bfs(x, y, count):
#     if(graph[x][y] == 0):
#         return 0

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     queue = deque([(x, y)])
#     graph[x][y] = 0

#     while(len(queue) > 0):
#         x, y = queue.popleft()
#         count += 1
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y

#             if(-1 < nx < N and -1 < ny < N and graph[nx][ny] == 1):
#                 queue.append((nx, ny))
#                 graph[nx][ny] = 0

#     return count

# graph = []
# for i in range(N):
#     row_str = input()
#     row = [int(i) for i in row_str]
#     graph.append(row)

# result = []
# for i in range(N):
#     for k in range(N):
#         count = bfs(i, k, 0)
#         if(count != 0):
#             result.append(count)


# result.sort()
# print(len(result))
# for i in result:
#     print(i)



def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if(x < 0 or y < 0 or x >= N or y >= N):
        return 0
    
    if(graph[x][y] == 0):
        return 0
    
    graph[x][y] = 0

    count = 1

    for i in range(4):
        count += dfs(dx[i] + x, dy[i] + y)
        
    return count
    
N = int(input())

graph = []
for i in range(N):
    row_str = input()
    row = [int(i) for i in row_str]
    graph.append(row)

result = []
for i in range(N):
    for k in range(N):
        count = dfs(i, k)
        if(count != 0):
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)