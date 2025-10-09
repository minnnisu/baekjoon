N = int(input())

rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort()

rope_size = len(rope)
answer = 0
for i in range(rope_size):
    answer = max(answer, rope[i] * (rope_size - i))

print(answer)