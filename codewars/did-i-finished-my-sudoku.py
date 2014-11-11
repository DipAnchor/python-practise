def done_or_not(board):
    if (heng(board) and shu(board) and square(board)):
        return 'Finished!'
    else:
        return 'Try again!'

def heng(board):
    for x in xrange(9):
        for x2 in xrange(9):
            if board[x].count(board[x][x2])!=1:
                return False
    return True
def shu(board):
    shu=[[] for i in range(9)]
    for y in xrange(9):
        for y2 in xrange(9):
             shu[y2].append(board[y][y2])
    return heng(shu)
def square(board):
    square=[[] for i in range(9)]
    for sh1 in xrange(3):
        for sl1 in xrange(3):
            square[0].append(board[sh1][sl1])
        for sl2 in xrange(3,6):
            square[1].append(board[sh1][sl2])
        for sl3 in xrange(6,9):
            square[2].append(board[sh1][sl3])
    for sh2 in xrange(3,6):
        for sl1 in xrange(3):
            square[3].append(board[sh2][sl1])
        for sl2 in xrange(3,6):
            square[4].append(board[sh2][sl2])
        for sl3 in xrange(6,9):
            square[5].append(board[sh2][sl3])
    for sh3 in xrange(6,9):
        for sl1 in xrange(3):
            square[6].append(board[sh3][sl1])
        for sl2 in xrange(3,6):
            square[7].append(board[sh3][sl2])
        for sl3 in xrange(6,9):
            square[8].append(board[sh3][sl3])
    return heng(square)
print shu([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])