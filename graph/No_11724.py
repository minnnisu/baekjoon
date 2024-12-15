from collections import deque 
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True

    while(len(queue) > 0):
        poped_node = queue.popleft()

        for node in graph[poped_node]:
            if(visited[node] == False):
                queue.append(node)
                visited[node] = True


count = 0
n, m = map(int,input().split(" "))
graph = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]

for i in range(m):
    u, v = map(int,input().split(" "))
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if(visited[i] == False):
        dfs(i, graph, visited)
        count += 1

print(count)