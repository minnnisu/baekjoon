hour, minute = map(int, input().split(" "))

if(minute < 45):
    if(hour < 1):
        hour = 23
    else:
        hour = hour - 1
    minute = 60 - (45 - minute)
else:
    minute = minute - 45
    
print(hour, minute)