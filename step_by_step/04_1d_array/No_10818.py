size = int(input())
arr = list(map(int, input().split(" ")))

#solve 1
# min_num = arr[0]
# max_num = arr[0]

# for i in range(1,size):
#     if(min_num > arr[i]):
#         min_num = arr[i]
#     if(max_num < arr[i]):
#         max_num = arr[i]
        
# print(min_num, max_num)

#solve 2
arr.sort()
print(arr[0], arr[-1])