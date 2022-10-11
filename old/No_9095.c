/* 
9059번 - 1,2,3 더하기
https://www.acmicpc.net/problem/9095
*/


#include<stdio.h>

int main()
{
    int T;
    scanf("%d", &T);

    int dp[11], temp;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for(int i = 4; i<=10; i++){
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
    }

    for(int i = 0; i<T; i++){
        scanf("%d", &temp);
        printf("%d\n", dp[temp]);
    }
}