# TLE

# ex:
# 123
# 456
# 789

sheetSize, turns = map(int, input().split())
bingoBalls = list(map(int, input().split()))

bingoSheet = [False] * sheetSize * sheetSize

#def isBingo(sheetSize, bingoSheet):
#    # check row
#    for row in range(sheetSize):
#        if False not in bingoSheet[sheetSize*row : sheetSize* (row+1)]:
#            return True
#
#    # check column
#    for column in range(sheetSize):
#        if False not in bingoSheet[column :: sheetSize]:
#            return True
#
#    # check left top to right bottom
#    isDiagonalBingo = True
#    for i in range(sheetSize):
#        isDiagonalBingo &=  bingoSheet[sheetSize * i + i]
#    if isDiagonalBingo:
#        return True
#
#    # check right top to left bottom
#    isDiagonalBingo = True
#    for i in range(sheetSize):
#        isDiagonalBingo &=  bingoSheet[sheetSize * (i+1) - (i+1)]
#    if isDiagonalBingo:
#        return True
#
#    # not bingo
#    return False

def isBingo(sheetSize, bingoSheet, ball):
    index = ball -1

    # check row -
    row = index // sheetSize
    if False not in bingoSheet[sheetSize*row : sheetSize* (row+1)]:
        return True

    # check colomn |
    column = index % sheetSize
    if False not in bingoSheet[column :: sheetSize]:
        return True

    # check left top to right bottom
    isDiagonalBingo = True
    for i in range(sheetSize):
        isDiagonalBingo &=  bingoSheet[sheetSize * i + i]
    if isDiagonalBingo:
        return True

    # check right top to left bottom
    isDiagonalBingo = True
    for i in range(sheetSize):
        isDiagonalBingo &=  bingoSheet[sheetSize * (i+1) - (i+1)]
    if isDiagonalBingo:
        return True

    # not bingo
    return False


for i, ball in enumerate(bingoBalls):
    bingoSheet[ball-1] = True

    if (isBingo(sheetSize, bingoSheet, ball)):
        print(i+1)
        exit(0)

print(-1)
