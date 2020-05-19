/*
Problem info
- 1977번 : 완전제곱수
- https://www.acmicpc.net/problem/1977

Idea
- Math(수학)

Solution
- 먼저 m과 가장 근접하면서 같거나 큰 완전제곱수를 찾는다
- m값을 1증가 시키면서 n에 가장 근접한 값에 도달할 때 까지 sum에 m*m의 값을 저장한다.
*/



#include<stdio.h>

int Closest_Sqrt(int start, int temp){
    int i = start;
    while(i*i <= temp){
        i++;
    }

    i--;

    if(i*i == temp){
        return i;
    }else{
        return i+1;
    }
}


int main()
{   
    int m,n;
    int sum = 0;
    int min = 0;
    scanf("%d %d", &m, &n);

    int m_sqrt = Closest_Sqrt(1,m);
    int i = m_sqrt;

    while(i*i <= n){
        sum += i*i;
        i++; 
    }

    if(sum > 0){
        printf("%d\n", sum);
        printf("%d", m_sqrt*m_sqrt);
    }else{
        printf("%d", -1);
    }
}
