N = int(input())
chess = [-100 for _ in range(N)]
answer = 0

def backtracking(x1, cnt):
    if(cnt == N):
        global answer
        answer += 1
        return
    
    for y in range(N):
        is_conflit = False
        for x2 in range(x1):
            if(y == chess[x2] or (x1 - x2 == y - chess[x2] or x1 - x2 == chess[x2] - y)):
                is_conflit = True
                break
            
        if not is_conflit:
            chess[x1] = y
            backtracking(x1 + 1, cnt + 1)
            chess[x1] = -100

backtracking(0, 0)
print(answer)