arr = [[1 for col in range(15)] for row in range(15)] #15*15개 이차원 리스트
for i in range(1, 15): #0층 초기화
    arr[0][i] = i;

for i in range(1,15):
    for j in range(2,15):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]


T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n])