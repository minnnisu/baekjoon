def get_hansu(n): #한수의 개수 반환
    count = 99
    if(n < 100):
        return n
    
    for i in range(100, n+1):
        num_0 = i%10
        num_1 = (i // 10)%10
        num_2 = i // 100
        
        if((num_0 - num_1) == (num_1-num_2)):
            count+=1
            
    return count
        
    
n = int(input())
print(get_hansu(n))