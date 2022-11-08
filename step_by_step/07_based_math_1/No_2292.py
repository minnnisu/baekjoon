n = int(input())
n_round = 1 #지나야 할 방의 개수
room_max = 1 #가장 큰 방의 번호 

if(n == 1):
    print(1)
else:
    while True:
        room_max = room_max + (6*n_round)
        n_round += 1
        if(n <= room_max):
            break;
    print(n_round)