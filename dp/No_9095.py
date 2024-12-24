def solution(n):
    dp = [0, 1, 2, 4]

    # if(n < 4):
    #     return dp[n] - 1
        
    for i in range(4, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    
    return dp[n]

t = int(input())

for i in range(t):
    n = int(input())
    print(solution(n))