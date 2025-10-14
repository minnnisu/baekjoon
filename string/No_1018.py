n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(input().strip()))

def repaint(chess, start):
    cnt = 0
    for i in range(8):
        current = start
        for color in chess[i]:
            if(color != current):
                cnt += 1
            if(current == "W"):
                current = "B"
            else:
                current = "W"
        if(start == "W"):
            start = "B"
        else:
            start = "W"
    
    return cnt


min_cnt = int(1e9)
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        temp_chess = [chess[k][j:j + 8] for k in range(i, i + 8)]
        min_cnt = min(min_cnt, repaint(temp_chess, "W"))
        min_cnt = min(min_cnt, repaint(temp_chess, "B"))

print(min_cnt)