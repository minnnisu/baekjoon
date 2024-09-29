n, k = map(int, input().split(" "))
start = 0
circle = [i for i in range(1, n + 1)]
result = []
result.append("<")

while True:
    start += (k - 1)
    start = start % len(circle)

    result.append(circle[start])
    result.append(", ")
    del circle[start]

    if(len(circle) < 1) :
        break

    start = start % len(circle)

result.pop()
result.append(">")

for result_element in result:
    print(result_element, end="")