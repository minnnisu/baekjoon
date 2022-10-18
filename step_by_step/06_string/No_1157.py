txt = input()
alphabet = [0 for i in range(26)]

for idx, ch in enumerate(txt):
    ch = ch.lower()
    alphabet[ord(ch) - 97] += 1
    
max_num = max(alphabet)
if(alphabet.count(max_num) > 1):
    print("?")
else:
    print(chr(65 + alphabet.index(max_num)))