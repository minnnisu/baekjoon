def binary_search(array, target, start, end):
    if(start > end):
        return 0
    
    mid = (start + end) // 2

    if(array[mid] == target):
        return 1
    
    elif(array[mid] < target):
        return binary_search(array, target, mid + 1, end)
    
    else:
        return binary_search(array, target, start, mid - 1)


N = int(input())
n_list = list(map(int, input().split(" ")))
n_list.sort()

M = int(input())
m_list = list(map(int, input().split(" ")))

for i in m_list:
    print(binary_search(n_list, i, 0, N -1))