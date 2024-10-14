from collections import deque

count = 0

def bfs(start): 
    global count
    queue = deque([start])
    visited[start] = True
    
    while(len(queue) > 0):
        poded_node = queue.popleft()
        count += 1
        for node in graph[poded_node]:
            if(visited[node] == False):
                queue.append(node)
                visited[node] = True

def dfs(start):
    global count
    count += 1
    visited[start] = True

    for node in graph[start]:
        if(visited[node] == False):
            dfs(node)



N = int(input())
M = int(input())

graph = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
# bfs(1)

print(count - 1)