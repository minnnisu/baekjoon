N = int(input())
deque = []
result = []

def execute(command, value):
    if(command == "push_front"):
        deque.insert(0, value)
    if(command == "push_back"):
        deque.append(value)
    if(command == "pop_front"):
        if(len(deque) == 0):
            print("-1")
        else:
            print(deque.pop(0))
    if(command == "pop_back"):
        if(len(deque) == 0):
            print("-1")
        else:
            print(deque.pop())
    if(command == "size"):
        print(len(deque))
    if(command == "empty"):
        if(len(deque) == 0):
            print("1")
        else:
            print("0")
    if(command == "front"):
        if(len(deque) == 0):
            print("-1")
        else:
            print(deque[0])
    if(command == "back"):
        if(len(deque) == 0):
            print("-1")
        else:
            print(deque[-1])


for i in range(N):
    command = input().split(" ")
    if(len(command) == 2):
        execute(command[0], command[1])
    else:
        execute(command[0], None)