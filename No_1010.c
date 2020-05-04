/*
Problem info 
- 1010번 - 다리놓기
- https://www.acmicpc.net/problem/1010

Idea
- DP(동적계획법)

Solution
- 점화식을 이용하여 문제를 해결
- 점화식 : dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
*/


#include<stdio.h>

int main()
{
    int dp[31][31]; //행: 서쪽 강, 열: 동쪽 강
    for(int i = 1; i<=30; i++){
        dp[i][0] = 0;
    }

    for(int i = 1; i<=30; i++){ //Base
            dp[1][i] = 1;
    }

    for(int i = 2; i<=30; i++){
        for(int j=1; j<=30; j++){
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]; //점화식
        }
    }

    int T,a,b; //T는 testcase의 갯수, a와b는 testcase
    scanf("%d", &T);

    for(int i=0; i<T; i++){ //반복문을 통해 testcase를 입력받은 후 알맞은 값을 출력
        int sum = 0; //N == a & M == b일 때 가능한 경우의 수
        scanf("%d %d", &a, &b);

        for(int i = 1; i<=b; i++){
            sum += dp[a][i];
        } 

        printf("%d\n", sum);
    }
}