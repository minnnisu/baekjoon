def count_tile(n):
    tile = [0, 1, 3]
    if(n == 1):
        return tile[1]
    
    if(n == 2):
        return tile[2]

    for i in range(3, n + 1):
        tile.append((tile[i - 2] * 2) + tile[i - 1])
    
    return tile.pop()
     

n = int(input())
print(count_tile(n) % 10007)