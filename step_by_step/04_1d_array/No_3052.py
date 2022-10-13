arr = [0 for i in range(42)]
count = 0

for i in range(10):
    num = int(input())
    arr[num % 42] += 1
for i in arr:
    if(i > 0):
        count += 1
        
print(count)