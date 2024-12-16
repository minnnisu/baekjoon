import sys
input = sys.stdin.readline

sum  = 0
count = 0
start = 0
end = 0

n, m = map(int, input().split(" "))
n_list = list(map(int, input().split(" ")))

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