t = int(input())
result = []
for i in range(t):
    iter_size, txt = input().split(" ")
    new_txt = ""
    for ch in txt:
        new_txt += ch * int(iter_size)
    result.append(new_txt)
        
for i in result:
    print(i)
