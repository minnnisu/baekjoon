a, b, v = map(int, input().split(" "))

#day(a-b) + a > v 

day = (v-a)/(a-b)
if(day != int(day)):
    day = int(day) + 1
else:
    day = int(day)

print(day + 1);