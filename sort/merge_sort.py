def merge_sort(array):
    if(len(array) < 2):
        return array
    
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    left = 0
    right = 0
    sorted_array = []

    while(left < len(left_array) and right < len(right_array)):
        if(left_array[left] < right_array[right]):
            sorted_array.append(left_array[left])
            left += 1
        else:
            sorted_array.append(right_array[right])
            right += 1
    
    sorted_array += (left_array[left:])
    sorted_array += (right_array[right:])

    return sorted_array


array = [1, 3, 2, 6, 5]

print(merge_sort(array))