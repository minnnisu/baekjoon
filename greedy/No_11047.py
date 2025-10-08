n, k = map(int, input().split(" "))
coins = []

for _ in range(n):
    coins.append(int(input()))

idx = len(coins) - 1
cnt = 0
while True:
    if(k == 0):
        break
    
    cnt += k // coins[idx]
    k = k % coins[idx]
    idx -= 1

print(cnt)