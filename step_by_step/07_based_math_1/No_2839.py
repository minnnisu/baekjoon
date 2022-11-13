T = int(input())
basket = [-1 for i in range(5001)];
size_1, size_2 = 0, 0

#base
basket[3] = 1;
basket[4] = -1;
basket[5] = 1;

for i in range(6, 5001):
    if(basket[i-5] == -1):
        size_1 = -1
    else:
        size_1 = basket[5] + basket[i-5];
    
    if(basket[i-3] == -1):
        size_2 = -1
    else:
        size_2 = basket[3] + basket[i-3];
        
    if(size_1 == -1 and size_2 == -1):
        basket[i] = -1;
    elif(size_1 == -1 and size_2 != -1):
        basket[i] = size_2
    elif(size_1 != -1 and size_2 == -1):
        basket[i] = size_1
    else:
        basket[i] = min(size_1, size_2)
        
print(basket[T])