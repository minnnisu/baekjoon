arr = []
for i in range(9):
    arr.append(int(input()))

max_num = arr[0]
max_idx = 0

for i in range(1,9):
    if(max_num < arr[i]):
        max_num = arr[i]
        max_idx = i
        
print(max_num)
print(max_idx+1)