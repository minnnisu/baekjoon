N = int(input())
rank_list = list()
result = [0 for i in range(N)]

for i in range(N):
    x, y = map(int, input().split(" "))
    rank_list.append((x, y))

for i in range(N):
    x = rank_list[i][0]
    y = rank_list[i][1]
    rank = 0
    for k in range(N):
        if(rank_list[k][0] > x and rank_list[k][1] > y):
            rank += 1
    result[i] = rank

for result_element in result:
    print(result_element + 1, end=" ")
