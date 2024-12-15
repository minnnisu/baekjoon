N = int(input())

costs = []
for i in range(N):
    rgb = list(map(int, input().split(" ")))
    costs.append(rgb)

for i in range(N-2, -1, -1):
    costs[i][0] += min(costs[i+1][1], costs[i+1][2])
    costs[i][1] += min(costs[i+1][0], costs[i+1][2])
    costs[i][2] += min(costs[i+1][0], costs[i+1][1])

print(min(costs[0][0], costs[0][1], costs[0][2]))