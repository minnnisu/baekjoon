N = int(input())
sequences = []
operators = []
min_value = 1000000000
max_value = -1000000000

sequences = list(map(int, input().split(" ")))
operators = list(map(int, input().split(" ")))

def calculate(a, i, b):
    if i == 0:
        return a + b
    if i == 1:
        return a - b
    if i == 2:
        return a * b
    if i == 3:
        if(a < 0):
            return -((-a) // b)
        else:
            return a // b

    

def backtracking(cnt, result):
    if cnt == len(sequences) - 1:
        global min_value
        global max_value

        min_value = min(result, min_value)
        max_value = max(result, max_value)
        return
    
    for i in range(4):
        if(operators[i] > 0):
            operators[i] -= 1
            tmp_result = calculate(result, i, sequences[cnt + 1])
            backtracking(cnt + 1, tmp_result)
            operators[i] += 1 
        

backtracking(0, sequences[0])
print(max_value)
print(min_value)

