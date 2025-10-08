import heapq
N = int(input())
M = int(input())

INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, w = map(int, input().split(" "))
    graph[a].append((b, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if(distance[now] < dist):
            continue

        for node in graph[now]:
            next, wei = node
            next_dist = wei + dist

            if(next_dist < distance[next]):
                heapq.heappush(q, (next_dist, next))
                distance[next] = next_dist

s, e = map(int, input().split(" "))
dijkstra(s)
print(distance[e])