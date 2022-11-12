T = int(input())

for i in range(T):
    h, w, n = map(int,input().split(" "))
    front = (n%h)*100 #고객의 호실의 앞자리
    back = n//h #고객의 호실의 뒷자리
    
    if(front == 0):
        print(h*100 + back)
    else:
        print(front+back+1)