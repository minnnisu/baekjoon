n = int(input())
k = 0
movement = []
def hanoi(n, start, to, end):
    if(n == 0):
        return
    
    hanoi(n - 1, start, end, to)
    movement.append((start, end))
    global k
    k += 1
    hanoi(n - 1, to, start, end)

hanoi(n, 1, 2, 3)
print(k)
for move in movement:
    print(f"{move[0]} {move[1]}")