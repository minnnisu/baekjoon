import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
n_list = list(map(int, input().split(" ")))

start = 0
end = 0
sum = 0
count = 0

while(start < n):
    if(sum >= m or end == n):
        sum -= n_list[start]
        start += 1
    else:
        sum += n_list[end]
        end += 1
    
    if(sum == m):
        count += 1

print(count)