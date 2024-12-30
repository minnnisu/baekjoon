from collections import deque

def dfs(now):
    if(visited[now]):
        return

    visited[now] = True
    print(now, end=" ")

    for node in graph[now]:
        dfs(node)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        podded_node = queue.popleft()
        print(podded_node, end=" ")
        
        for node in graph[podded_node]:
            if(visited[node] == False):
                queue.append(node)
                visited[node] = True



n, m, v = map(int, input().split(" "))

graph = [[] for i in range(n + 1)]
for i in range(m):
    node1, node2 = map(int, input().split(" "))
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in graph:
    i.sort()

visited = [False for i in range(n + 1)]
dfs(v)
print()

visited = [False for i in range(n + 1)]
bfs(v)