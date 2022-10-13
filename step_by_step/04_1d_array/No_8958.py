n = int(input())
result = []

for i in range(n):
    case = input()
    total_score = 0
    current_score = 0
    count = 1
    for i in case:
        if(i == 'O'):
            total_score += count
            count += 1
        else:
            count = 1
    result.append(total_score)
    total_score = 0
    current_score = 0
    count = 1
    
for i in result:
    print(i)