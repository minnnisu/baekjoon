txt = input()
alphabet = [-1 for i in range(26)]

for idx, i in enumerate(txt):
    if(alphabet[ord(i) - 97] == -1): #해당 알파벳이 처음 나타난 경우
        alphabet[ord(i) - 97] = idx
        
for i in alphabet:
    print(i, end=" ")
print()