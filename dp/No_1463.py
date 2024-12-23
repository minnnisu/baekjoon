import sys
input = sys.stdin.readline

def solution(n):
    dp = [0, 0]

    for i in range(2, n + 1):
        min = dp[i - 1]

        if(i % 3 == 0 and min > dp[i // 3]):
            min = dp[i // 3]

        if(i % 2 == 0 and min > dp[i // 2]):
            min = dp[i // 2]

        dp.append(min + 1)

    return dp[n]
    
n = int(input())

print(solution(n))