/*
Problem info
- 1475번 : 방 번호
- https://www.acmicpc.net/problem/1475

Idea
- Math(수학)

Solution
- 입력받은 수의 각자리를 분리한 후 각 숫자들 빈도를 배열에 저장한다.
- 6과 9의 합의 절반과 6과 9를 제외한 나머지 숫자들의 빈도 중
가장 큰 값을 구한다
- 마지막으로 둘중에 큰 수를 출력한다.
***n이 0일경우를 잘 생각해야 됨***
*/


#include<stdio.h>

int Max(int a, int b){ //최댓갑을 리턴하는 함수
    if(a>=b){
        return a;
    }else{
        return b;
    }
}

int main() {
    int n, temp; // 0<=n<=1,000,000
    scanf("%d", &n);
    int num[10] = { 0 }; //0~9까지 
    while (n != 0) {  
        temp = n % 10; //n의 각자리 수를 분리한 후
        num[temp] += 1; //그 수에 해당하는 인덱스의 값을 1증가 시킴
        n = n / 10;
    }

    int max = 0; //0~5,7,8 중 가장 높은 빈도를 담는 변수

    for(int k = 0; k<10; k++){
        if(k!=6 && k!=9 && num[k] > max){
            max = num[k]; 
        }
    }

    int sixAndnine, ans;
    if((num[6] + num[9]) % 2 == 1){ //6과 9의 합이 홀수일 경우
        sixAndnine = ((num[6] + num[9])/2)+1; // 그 값의 절반을 반올림 해줌
    }else{
        sixAndnine = (num[6] + num[9])/2;
    }

    ans = Max(max, sixAndnine);

    if(ans == 0){ //입력받은 n이 0일 경우
        ans = 1;
    }

    printf("%d", ans);

    

}