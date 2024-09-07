n, m = map(int, input().split(" "))

n_list = [0 for i in range(n+1)]

for a in range(m):
    i, j, k = map(int, input().split(" "))
    for b in range(i, j+1):
        n_list[b] = k

del n_list[0]
for n in n_list:
    print(n, end=" ")