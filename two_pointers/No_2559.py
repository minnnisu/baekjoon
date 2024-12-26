n, k = map(int, input().split(" "))
n_list = list(map(int, input().split(" ")))

sum = 0
max = 0
start = 0
end = k - 1

for i in range(start, end + 1):
    sum += n_list[i]
max = sum

while True:
    end += 1
    if(end >= n):
        break

    sum -= n_list[start]
    sum += n_list[end]
    start += 1

    if(sum > max):
        max = sum        

print(max)