N = int(input())
fill_space = []
count = 0
for i in range(100):
    row = []
    for j in range(100): 
        row.append(0)
    fill_space.append(row)

for i in range(N):
    x, y = map(int, input().split(" "))

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if(fill_space[i][j] == 0):
                count += 1
                fill_space[i][j] = 1

print(count)