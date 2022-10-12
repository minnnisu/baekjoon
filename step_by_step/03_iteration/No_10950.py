count = int(input())

result = []

for i in range(count):
    a, b = map(int,input().split(" "))
    result.append(a+b)

for i in result:
    print(i);