n = int(input())
numbers_stack = [] # 돈을 담는 스택

for i in range(n):
    number = int(input()) 
    if(number == 0 and len(numbers_stack) > 0): # 0을 부를 경우
        numbers_stack.pop()
    else:
        numbers_stack.append(number)

sum = 0
for number in numbers_stack:
    sum += number

print(sum)