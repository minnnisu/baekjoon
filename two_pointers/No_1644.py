import sys
input = sys.stdin.readline

def get_demical(n):
    n_list = [x for x in range(n + 1)]
    decimal = []
    for i in range(2, n + 1):
        if(n_list[i] == -1):
            continue
    
        decimal.append(i)
        k = 2
        while(i * k <= n):
            n_list[i * k] = -1
            k += 1

    return decimal

def two_pointers(n, array):
    start = 0
    end = 0
    sum = 0
    count = 0

    while(start < len(array)):
        if(sum >= n or end == len(array)):
            sum -= array[start]
            start += 1
        else:
            sum += array[end]
            end += 1

        if(sum == n):
            count += 1
    
    return count

n = int(input())
decimal = get_demical(n)
print(two_pointers(n, decimal))