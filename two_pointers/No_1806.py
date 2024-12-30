import sys
input = sys.stdin.readline

n, s = map(int, input().split(" "))
n_list = list(map(int, input().split(" ")))

start = 0
end = 0
sum = 0
s_length = 100001

while start < n:
    if(sum >= s or end == n):
        sum -= n_list[start]
        start += 1
    else:
        sum += n_list[end]
        end += 1

    length = end - start  
    if(sum >= s and length < s_length):
        s_length = length

if(s_length == 100001):
    print(0)
else:
    print(s_length)