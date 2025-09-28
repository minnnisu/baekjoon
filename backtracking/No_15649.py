N, M = map(int, input().split(" "))
numbers = []

def backtracking(cnt):
    if(cnt == M):
        for number in numbers:
            print(number, end=" ")
        print()
        return
    
    for i in range(1, N + 1):
        if(i not in numbers):
            numbers.append(i)
            backtracking(cnt + 1)
            numbers.pop()

backtracking(0)



