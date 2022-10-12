import sys

count = int(sys.stdin.readline())

result = []

for i in range(count):
    a, b = map(int,sys.stdin.readline().split(" "))
    result.append(a+b)

for idx, i in enumerate(result):
    print("Case #{}: {}".format(idx+1, i));