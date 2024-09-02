s = input() 

result = int(s[0])

for i in range(1, len(s)):
    target = int(s[i])
    if(result > 1 and target > 1 ):
        result *= target
    else:
        result += target

print(result)