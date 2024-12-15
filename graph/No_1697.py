from collections import deque

def bfs(n, k):
    queue = deque([(n, 0)])
    visited = [False for i in range(100001)]

    if(n == k):
        return 0

    while(len(queue) > 0):
        poded_node, count = queue.popleft()
        count += 1

        double = 2 * poded_node
        plus1 = poded_node + 1
        minus1 = poded_node - 1
        
        if(plus1 == k or minus1 == k or double == k):
            return count
        
        if(plus1 <= 100000 and visited[plus1] == False):
            queue.append((plus1, count))
            visited[plus1] = True

        if(0 <= minus1 <= 100000 and visited[minus1] == False):
            queue.append((minus1, count))
            visited[minus1] = True

        if(double <= 100000 and visited[double] == False):
            queue.append((double, count))
            visited[double] = True
        
n, k =  map(int, input().split(" "))

print(bfs(n, k))