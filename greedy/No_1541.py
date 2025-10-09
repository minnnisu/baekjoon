expressions = list(input().split("-"))

answers = []
for expression in expressions:
    values = list(map(int, expression.split("+")))
    sum = 0
    for value in values:
        sum += value
    answers.append(sum)

answer = answers[0]
for i in range(1, len(answers)):
    answer -= answers[i]

print(answer)