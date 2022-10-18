def getTime(ch):
    if(ch <= 'O'):
        code = ord(ch) - 65
        return 3 + (code // 3)
    elif(ch <= 'S'):
        return 8
    elif(ch <= 'V'):
        return 9
    else:
        return 10

txt = input()
total = 0

for ch in txt:
    total += getTime(ch)
    
print(total)
