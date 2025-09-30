import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split(" ")))
liquid.sort()

start = 0
end = len(liquid) - 1
answer = (liquid[start], liquid[end])
answer_sum = abs(answer[0] + answer[1])


while start < end :
    sum = liquid[start] + liquid[end]

    if answer_sum > abs(sum):
        answer = (liquid[start], liquid[end])
        answer_sum = abs(sum)

        if(answer == 0):
            break

    if(sum < 0):
        start += 1
    else:
        end -= 1

print(f"{answer[0]} {answer[1]}")