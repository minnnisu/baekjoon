#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
king, queen, rook, bishop, knight, pawn = map(int, input().split(" "))

print(1-king, end=" ")
print(1-queen, end=" ")
print(2-rook, end=" ")
print(2-bishop, end=" ")
print(2-knight, end=" ")
print(8-pawn)