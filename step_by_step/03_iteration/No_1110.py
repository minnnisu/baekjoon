n = int(input())
tmp = n
count = 0

while True:
    a = (tmp // 10) + (tmp % 10)
    tmp = ((tmp % 10) * 10) + (a % 10)
    count = count + 1
    if(tmp == n):
        break
    
print(count)