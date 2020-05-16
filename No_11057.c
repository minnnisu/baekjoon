/*
Problem info
- 11057번 : 오르막 수
- https://www.acmicpc.net/problem/11057

Idea
- Math(수학)
- DP(동적계획법)

Solution
- 점화식을 이용하여 해결
- 점화식 : dp[j] = dp[j - 1] + dp[j]
- Base : dp[i] 1 (0<=i<=9)
*/




#include<stdio.h>

int main()
{
    int n, sum;
    sum = 1;
    scanf("%lld", &n);
    int dp[10];
    for (int i = 0; i < 10; i++) {
        dp[i] = 1;
    }

    for (int i = 2; i <= n; i++) {
        for (int j = 1; j < 10; j++) {
            dp[j] = (dp[j - 1] + dp[j])%10007;
            if (i == n) {
                sum += dp[j];
            }
        }
    }

    if (n == 1) {
        sum = 10;
    }

    printf("%d", sum % 10007);
}