N = int(input())

meeting = []
for _ in range(N):
    s, e = map(int, input().split(" "))
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0]))
answer = 0
end = 0

for ns, ne in meeting:
    if(ns >= end):
        end = ne
        answer += 1

print(answer)
