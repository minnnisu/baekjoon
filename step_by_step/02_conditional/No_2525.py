hour, minute = map(int, input().split(" "))
cook_time = int(input())

cook_hour = int(cook_time / 60)
cook_minute = cook_time % 60

hour = hour + cook_hour
minute = minute + cook_minute

if(minute > 59):
    hour = hour + int(minute / 60)
    minute = minute % 60

if(hour > 23):
    hour = hour % 24
    
print(hour, minute)