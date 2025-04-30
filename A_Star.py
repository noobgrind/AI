import heapq

def heuristic(board, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            distance += abs(i-x) + abs(j-y)
    return distance

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i,j

def move_blank(board,direction):
    i, j = find_blank(board)
    new_board = [row[:] for row in board]
    
    if direction == "up" and i > 0:
        new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
    elif direction == "down" and i < 2:
        new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
        
    elif direction == "left" and j > 0:
        new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
    elif direction == "right" and j < 2:
        new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
    else:
        return None
    
    return new_board

def a_star(start,goal):
    queue = []
    visited = set()
    
    h = heuristic(start,goal)
    heapq.heappush(queue, (h,0,start,[]))
    
    while queue:
        f, g, board, path = heapq.heappop(queue)
        
        if board == goal:
            print("Solved in ", g, " Moves.")
            print("Path : ", path)
            return
        
        board_tup = tuple(tuple(row) for row in board)
        visited.add(board_tup)
        
        for move in ["up", "down", "left", "right"]:
            new_board = move_blank(board,move)
            
            if new_board is not None:
                new_board_tup = tuple(tuple(row) for row in new_board)
                if new_board_tup not in visited:
                    new_g = g + 1
                    new_h = heuristic(new_board,goal)
                    new_f = new_h + new_g
                    heapq.heappush(queue, (new_f, new_g, new_board, path + [move]))
    
    print("No Solution Found.")
        

start = [[1,2,3],
         [4,0,5],
         [6,7,8]]

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

print(heuristic(start,goal))
print(find_blank(start))
print(move_blank(start,"down"))
a_star(start,goal)