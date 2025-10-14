n = int(input())
words = [[] for _ in range(51)]
for _ in range(n):
    word = input()
    if(word not in words[len(word)]):
        words[len(word)].append(word)

for word_row in words:
    word_row.sort()

    for word in word_row:
        print(word)