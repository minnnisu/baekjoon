import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split(" ")))
x = int(input())

start = 0
end = n - 1
count = 0
n_list.sort()

while(start < end):
    if(n_list[start] + n_list[end] == x):
        count += 1

    if(n_list[start] + n_list[end] <= x):
        start += 1
    else:
        end -= 1

print(count)