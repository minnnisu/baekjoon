from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while(len(queue) > 0):
        poped_node = queue.popleft()
        
        for i in graph[poped_node]:
            if(visited[i] == False):
                visited[i] = True
                queue.append(i)


def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if(visited[i] == False):
            bfs(graph, i, visited)

def excute():
    M, N, K = map(int, input().split(" "))
    matrix = []
    for _ in range(N):
        row = []
        for _ in range(M):
            row.append(0)
        matrix.append(row)

    for i in range(K):
        y, x = map(int, input().split(" "))
        matrix[x][y] = 1

    graph = []
    visited = []
    count = 0
    for i in range(N * M + 1):
        graph.append([])
        visited.append(False)

    for i in range(N):
        for k in range(M):
            if(matrix[i][k] == 0):
                continue

            current_node = (M * i) + (k + 1)
            if(i - 1 > -1 and matrix[i - 1][k] == 1):
                graph[current_node].append((M * (i - 1)) + (k + 1))

            if(i + 1 < N and matrix[i + 1][k] == 1):
                graph[current_node].append((M * (i + 1)) + (k + 1))

            if(k - 1 > -1 and matrix[i][k - 1] == 1):
                graph[current_node].append((M * i) + (k))

            if(k + 1 < M and matrix[i][k + 1] == 1):
                graph[current_node].append((M * i) + (k + 2))
                
    for i in range(N):
        for k in range(M):
            current_node = (M * i) + (k + 1)
            if(matrix[i][k] == 1 and visited[current_node] == False):
                count += 1
                bfs(graph, current_node, visited)

    print(count)

T = int(input())
for _ in range(T):
    excute()