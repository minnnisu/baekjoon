import sys
input = sys.stdin.readline


def solution(n, stair):
    if(n == 1):
        return stair[1]
    
    if(n == 2):
        return stair[1] + stair[2]
    
    dp = [0, stair[1], stair[1] + stair[2]]
    for i in range(3, n + 1):
        dp.append(max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i]))

    return dp[n]

n = int(input())
stair = [0]

for i in range(n):
    stair.append(int(input()))

print(solution(n, stair))