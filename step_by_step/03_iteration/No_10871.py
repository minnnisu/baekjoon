size, target = map(int, input().split(" "))

numbers = list(map(int, input().split(" ")))
for idx, i in enumerate(numbers):
    if(i >= target):
        numbers[idx] = - 1
        
for i in numbers:
    if(i != -1):
        print(i, end=" ")