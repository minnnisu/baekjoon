def d(n):
    sum_num = n #n과 n의 각자리를 더한 결과
    while n != 0: #각자리 수를 합한다
        sum_num += n%10
        n = n // 10
    return sum_num 

self_num = [0 for i in range(10001)]
for i in range(10001):
    num = d(i) #n과 n의 각자리를 더한 결과 반환
    if(num <= 10000): # out of range 방지
        self_num[num] = 1 #셀프넘버가 아닌 수의 인덱스를 1로 저장

for i in range(1,10001): #셀프넘버 출력
    if(self_num[i] == 0):
        print(i)