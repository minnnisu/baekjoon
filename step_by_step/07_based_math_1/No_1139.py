def root_calc(a,b,c): #근의 공식
    r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    plus_num = max(r1, r2)
    if(plus_num != int(plus_num)):
        plus_num = int(plus_num) + 1
        
    return int(plus_num)

pos = int(input())
divisor = 0 #분모
numerator = 0 #분자

n = root_calc(1,1,-1*(pos*2)) 
prev_sum = (n*(n-1)) // 2 
distance_pos = pos - prev_sum 
if(n % 2 == 0):
    divisor = (n+1) - distance_pos
    numerator = (n+1) - divisor
else:
    numerator = (n+1) - distance_pos
    divisor = (n+1) - numerator
    
print("{}/{}".format(numerator, divisor))