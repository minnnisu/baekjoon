def solution(n):
    dp = [-1, -1, -1, 1, -1, 1]

    for i in range(6, n + 1):
        if(dp[i - 5] < 0 and dp[i - 3] < 0):
            dp.append(-1)
        elif(dp[i - 5] >= 0 and dp[i - 3] >= 0):
            dp.append(min(dp[i - 5], dp[i - 3]) + 1)
        elif(dp[i - 5] == -1):
            dp.append(dp[i - 3] + 1)
        else:
            dp.append(dp[i - 5] + 1)

    return dp[n]

n = int(input())

print(solution(n))