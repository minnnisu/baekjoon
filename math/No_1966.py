from collections import deque

t = int(input())

def printer_queue(docs):
    q = deque(docs)
    cnt = 0
    while q:
        important = max(q)
        doc = q.popleft()
        if(important[0] > doc[0]):
            q.append(doc)
        else:
            cnt += 1
            if(doc[1] == 1):
                return cnt
                



for _ in range(t):
    n, m = map(int, input().split(" "))
    docs = list(map(int, input().split()))
    for i in range(n):
        if(i == m):
            docs[i] = (docs[i], 1)
        else:
            docs[i] = (docs[i], 0)
    print(printer_queue(docs))