n = int(input())
x_list = sorted(list(map(int, input().split(" "))))

count = 0
group = 0

for x in x_list:
    count += 1
    if(x <= count):
        group += 1
        count = 0

print(group)