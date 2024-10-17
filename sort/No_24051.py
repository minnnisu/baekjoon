import sys
 
input = sys.stdin.read # 한 번에 모든 내용 입력받음
data = input().split() # 공백 기준으로 분리
 
N = int(data[0])
K = int(data[1])
a_list = list(map(int, data[2:]))

def insertion_sort(a_list, k):
    count = 0
    for i in range(1, len(a_list)):
        new_item = a_list[i]
        loc = i - 1
        while (0 <= loc and new_item < a_list[loc]):
            a_list[loc + 1] = a_list[loc]
            loc -= 1

            count += 1
            if(k == count):
                print(a_list[loc + 1])
                return
    
        if(loc != i - 1):
            a_list[loc + 1] = new_item

            count += 1
            if(k == count):
                print(a_list[loc + 1])
                return
    
    print(-1)

insertion_sort(a_list, K)