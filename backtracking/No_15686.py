N, M = map(int, input().split(" "))
city = []
# 치킨집 목록(r,c)
chickens = []
# 행: 집, 열: 치킨집과 집 거리 목록
houses = []
m_chicken = []
answer = (50 * 50) * 2 * N

for _ in range(N):
    city.append(list(map(int, input().split(" "))))

for r in range(N):
    for c in range(N):
        if(city[r][c] == 2):
            chickens.append((r, c))

for r in range(N):
    for c in range(N):
        if(city[r][c] == 1):
            temp = []
            for chicken in chickens:
                temp.append(abs(chicken[0] - r) + abs(chicken[1] - c))
            houses.append(temp)
    

def backtracking(cnt):
    if(cnt == M):
        chicken_dist_of_city = 0
        for house in houses:
            chicken_dist = 50 * 50
            for chicken in m_chicken:
               chicken_dist = min(house[chicken], chicken_dist)

            chicken_dist_of_city += chicken_dist

        global answer
        answer = min(chicken_dist_of_city, answer)
        return

    for i in range(len(chickens)):
        if(len(m_chicken) < 1 or i > m_chicken[-1]):
            m_chicken.append(i)
            backtracking(cnt + 1)
            m_chicken.pop()

backtracking(0)
print(answer)