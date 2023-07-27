board = [
    [5,0,7,0,0,0,0,0,0],
    [0,0,0,0,8,0,0,0,9],
    [3,9,1,5,6,0,0,0,7],
    [0,0,3,1,0,5,0,0,8],
    [8,5,0,2,0,9,0,3,4],
    [1,0,0,6,0,8,5,0,0],
    [7,0,0,0,2,4,8,1,6],
    [9,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,2,0,3]]
def print_board(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("---------------------") #this prints a horizontal line between the bigger boxes
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print('|', end ='')
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+"",end="") #this prints a vertical line between the bigger boxes
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return(i,j)
    return None
def valid(board, num, position):
    for i in range(len(board[0])): #checking row
        if board[position[0]][i]==num and position[1]!=i:
            return False
    for j in range(len(board)): #checking column
        if board[i][position[1]]==num and position[0]!=i:
            return False
    box_x=position[1]//3
    box_y=position[0]//3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j]==num and (i,j)!=position:
                return False
    return True
def solve(board): #solving sudoku
    find=find_empty(board)
    if not find:
        return True
    else:
        row, col=find
    for i in range(1,10):
        if valid(board, i, (row, col)):
           board[row][col]=i
           if solve(board):
               return True
           board[row][col]=0
    return False
print_board(board)
solve(board)
print("solving")
print_board(board)
print("solved")