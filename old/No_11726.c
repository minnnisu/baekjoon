/*
Problem info
- 11726번 : 2xN 타일링
- https://www.acmicpc.net/problem/11726

Idea
- Math(수학)
- DP(동적계획법)

Solution
- 점화식을 이용하여 해결
- 점화식 : dp[n] = dp[n-1] + dp[n-2] (n>=3)
- Base : dp[1] = 1, dp[2] = 2
*/


#include<stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int dp[1001];
    dp[1] = 1;
    dp[2] =2;
    for(int i = 3; i<=n; i++){
        dp[i] = (dp[i-2] + dp[i-1]) % 10007; //피보나치 수열 이용
    }

    printf("%d", dp[n]);

    return 0;
    
}