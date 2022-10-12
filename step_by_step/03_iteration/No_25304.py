paid_money = int(input())
count = int(input())
total = 0

for i in range(count):
    price, amount = map(int, input().split(" "))
    total = total + (price * amount)
    
if(total == paid_money):
    print("Yes")
else:
    print("No")