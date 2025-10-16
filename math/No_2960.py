n, k = map(int, input().split())

checked = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if(checked[i] == 1):
        continue
    
    cnt += 1
    b = 1
    if(cnt == k):
        print(i * b)
    while(True):
        b += 1
        if(i * b > n):
            break

        if(checked[i * b] == 1):
            continue

        checked[i * b] = 1
        cnt += 1
        if(cnt == k):
            print(i * b)