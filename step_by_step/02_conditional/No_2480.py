a, b, c = map(int, input().split(" "))
victory_money = 0

if((a == b) and (b == c)): #모두 같은 경우
    victory_money = (a * 1000) + 10000
elif((a == b) or (b == c)): # a와 b 또는 b와 c가 같은 경우
    victory_money = (b * 100) + 1000
elif((a == c)): # a와 c가 같은 경우
    victory_money = (a * 100) + 1000
else: #모두 다른 경우
    if(a > b):
        victory_money = a
    else:
        victory_money = b
    if(c > victory_money):
        victory_money = c
    victory_money = victory_money * 100
    
print(victory_money)