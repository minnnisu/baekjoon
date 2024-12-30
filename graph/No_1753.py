import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) #(가중치, 노드 번호) 형태로 삽입

    while queue:
        distance[start] = 0
        dist, now = heapq.heappop(queue)
        
        if(distance[now] < dist):
            continue

        for node, next_dist in graph[now]:
            total_dist = dist + next_dist
            if(distance[node] > total_dist):
                distance[node] = total_dist
                heapq.heappush(queue, (total_dist, node))



V, E = map(int, input().split(" "))
K = int(input())

graph = [[] for _ in range(V + 1)]
distance = [1e9 for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split(" "))
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V + 1):
    if(distance[i] == 1e9):
        print("INF")
    else:
        print(distance[i])