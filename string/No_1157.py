# words = input()
# count = [0] * 26
# max_count = 0
# answer = ""

# for word in words:
#     if(ord(word) >= 97):
#         idx = ord(word) - 97
#         count[idx] += 1
    
#     elif(ord(word) >= 65):
#         idx = ord(word) - 65
#         count[idx] += 1

# for i in range(len(count)):
#     if(count[i] > max_count):
#         max_count = count[i]
#         answer = chr(65 + i)
#     elif(count[i] == max_count):
#         answer = "?"              

# print(answer)

words = input()
count = [0] * 26
max_count = 0
answer = ""

for word in words:
    uw_ord = ord(word.upper()) - 65
    count[uw_ord] += 1

max_count = max(count)
if(count.count(max_count) > 1):
    print("?")
else:
    print(chr(65 + count.index(max_count)))