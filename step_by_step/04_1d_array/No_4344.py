c = int(input())
result = []

for i in range(c):
    case = list(map(int, input().split(" ")))
    n = case[0]
    scores = case[1:]
    mean = sum(scores)/n
    count = 0
    for score in scores:
        if(score > mean):
            count += 1
    result.append((count / n)*100)
    
for i in result:
    print('{0:0.3f}%'.format(i))