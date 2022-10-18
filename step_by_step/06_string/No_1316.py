#Case 1
#내가 푼 방법

#flag == 1 -> 이미 등장
#flag == 0 -> 처음 등장
#flag == -1 -> 불연속적으로 나타남

T = int(input())
count = 0

for i in range(T):
    txt = input()
    flag = [0 for i in range(26)]
    prev = txt[0]
    flag[ord(prev) - 97] = 1

    for current in txt:
        if(prev != current): #이전 문자와 현재문자가 다를 때
            if(flag[ord(current) - 97] == 1): #이미 등장했을 경우
                flag[ord(current) - 97] = -1 # flag = -1
            elif(flag[ord(current) - 97] == 0): # 처음 등장했을 경우
                flag[ord(current) - 97] = 1 #flag = 1
        prev = current
        
    if(not (-1 in flag)):
        count += 1
        
print(count)

# #Case 2 
# #블로그 참조
# N = int(input())
# cnt = 0

# for i in range(N):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         elif word[j] in word[j+1:]: #부분집합을 구함
#             cnt -= 1
#             break

# print(cnt)