/*
Problem info
- 2163번 : 초콜릿 자르기
- https://www.acmicpc.net/problem/2163

Idea
- DP(동적계획법)

Solution
- 점화식을 통해 해결
- 점화식 : dp[i] = dp[i-1] + dp[1] + 1
- Base : dp[1] = N - 1
*/

#include<stdio.h>

int main()
{
    int a,b;
    scanf("%d %d", &a, &b);
    int dp[301];
    dp[1] = a-1;
    for(int i = 2; i<=b; i++){
        dp[i] = dp[i-1] + dp[1] + 1;
    }

    printf("%d", dp[b]);
}