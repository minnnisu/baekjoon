/*
Problem info
- 1699번 : 제곱수의 합
- https://www.acmicpc.net/problem/1699

Idea 
- DP(동적계획법)

Solution
- 점화식을 이용하여 해결
- 점화식 : dp[j] = min(dp[j], 1 + dp[j - temp])
  temp : n에 가장 근접한 제곱수
- Base : dp[0] = 0, dp[i] = i (1<=i<=n)
*/



#include<stdio.h>

int Closest_Sqrt(int temp) //temp에 가장 근접한 제곱 수 찾는 함수
{
    int a = 1;
    while (a * a <= temp)
    {
        a++;
    }

    return  a - 1;
}

int min(int a, int b) {
    if (a <= b) {
        return a;

    }
    else {
        return b;

    }
}

int main()
{
    int n, m;
    int dp[1000001];
    scanf("%d", &n);
    m = Closest_Sqrt(n);

    //base
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        dp[i] = i;
    }

    //점화식 이용
    for (int i = 2; i <= m; i++) {
        int temp = i * i;
        for (int j = temp; j <= n; j++) {
            dp[j] = min(dp[j], 1 + dp[j - temp]);
        }
    }

    printf("%d", dp[n]);

    return 0;
}