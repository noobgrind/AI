def isSafe(board, row, col, n):
    
    for i in range(n):
        if board[row][i] == 'Q':
            return False
    for i in range(n):
        if board[i][col] == 'Q':
            return False
        
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i-=1
        j-=1
    
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i-=1
        j+=1
    
    return True


def nQueens(board, row, n):
    
    for j in range(n):
        if row == n:
            for i in board:
                print(i)
            print()
            return
        
        if isSafe(board, row, j, n):
            board[row][j] = 'Q'
            nQueens(board, row+1, n)  
            board[row][j] = '.'




n = 5
board = [['.' for i in range(n)] for j in range(n)]
nQueens(board, 0, n)

