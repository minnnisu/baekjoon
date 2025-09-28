def backtracking(cnt):
    if(cnt == M):
        for number in numbers:
            print(number, end=" ")
        print()
        return
    
    for i in range(1, N + 1):
        if(len(numbers) == 0 or (len(numbers) > 0 and numbers[len(numbers) - 1] < i)):
            numbers.append(i)
            backtracking(cnt + 1)
            numbers.pop()


N, M = map(int,input().split(" "))
numbers = []

backtracking(0)
