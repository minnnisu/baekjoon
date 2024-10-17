def selection_sort(a_list, k):
    count = 0
    for i in range(len(a_list) - 1, 0, -1):
        max_index = i
        for j in range(0, i):
            if(a_list[max_index] < a_list[j]):
                max_index = j
                
        if(i != max_index):
            count += 1
            if(k == count):
                print(str(a_list[i]) + " " + str(a_list[max_index]))
                return
                
            a_list[i], a_list[max_index] =  a_list[max_index], a_list[i]

    print(-1)
       

N, K = map(int, input().split())
a_list = list(map(int, input().split(" ")))

selection_sort(a_list, K)