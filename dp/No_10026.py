import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, x, y, color, visited):
    if((-1 < x < N and -1 < y < N) == False):
        return

    if(graph[x][y] != color or visited[x][y]):
        return

    visited[x][y] = True
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        dfs(graph, dx[i] + x, dy[i] + y, color, visited)


normal = 0
saekyack = 0

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]
for x in range(N):
    for y in range(N):
        if(visited[x][y] == False):
            dfs(graph, x, y, graph[x][y], visited)
            normal += 1

for x in range(N):
    for y in range(N):
        if(graph[x][y] == "G"):
            graph[x][y] = "R"

visited = [[False for _ in range(N)] for _ in range(N)]
for x in range(N):
    for y in range(N):
        if(visited[x][y] == False):
            dfs(graph, x, y, graph[x][y], visited)
            saekyack += 1

print(f"{normal} {saekyack}")