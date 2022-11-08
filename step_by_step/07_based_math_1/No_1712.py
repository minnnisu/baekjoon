a, b, c = map(int, input().split(" "))

if(b >= c): #이익이 발생하지 않음
    print(-1)
else:
    break_even_point = int(a/(c-b)) + 1
    print(break_even_point)