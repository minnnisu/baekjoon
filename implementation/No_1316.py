# 그룹단어인지 확인하는 함수
def checkGroup(word):
    checked = [] # 각 사이클마다 나온 단어 리스트
    target = word[0] # 현재 체크중인 단어
    for char in word:
        if char != target:
            if(checked.count(char) == 1) :
                return False
            checked.append(target)
            target = char
    return True


n = int(input())
words = [] # 그룹단어 목록
count = 0 # 그룹 단어의 개수

for i in range(n):
    word = input()
    words.append(word)

for word in words:
    result = checkGroup(word)
    if(result):
        count += 1

print(count)