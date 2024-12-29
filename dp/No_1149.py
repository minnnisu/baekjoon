def solution(n, n_list):
    dp = [[], n_list[1]]

    for i in range(2, n + 1):
        dp.append([])
        dp[i].append(min(dp[i-1][1], dp[i-1][2]) + n_list[i][0])
        dp[i].append(min(dp[i-1][0], dp[i-1][2]) + n_list[i][1])
        dp[i].append(min(dp[i-1][0], dp[i-1][1]) + n_list[i][2])

    return min(dp[n][0], dp[n][1], dp[n][2])

n = int(input())
n_list = [[]]

for i in range(n):
    n_list.append(list(map(int, input().split(" "))))

print(solution(n, n_list))