from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")

    for node in graph[start]:
        if(visited[node] == False):
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    graph_deque = deque([start])
    visited[start] = True

    while len(graph_deque) > 0 :
        node = graph_deque.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if(visited[i] == False):
                visited[i] = True
                graph_deque.append(i)

N, M, V = map(int, input().split(" "))

graph = []
visited_bfs = []
visited_dfs = []
for i in range(N + 1):
    visited_dfs.append(False)
    visited_bfs.append(False)
    graph.append([])

for i in range(M):
    node1, node2 = map(int, input().split(" "))
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, N + 1):
    graph[i].sort()

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)