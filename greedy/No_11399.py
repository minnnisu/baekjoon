N = int(input())
p = list(map(int, input().split(" ")))
p.sort()

answer = 0
temp = 0
for pi in p:
    temp += pi
    answer += temp

print(answer)
