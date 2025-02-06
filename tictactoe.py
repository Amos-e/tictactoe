#Tic Tac Toe
import random as rd
board = [
            [1,2,3],
            [4,"X",6],
            [7,8,9]
        ]

def print_board(board):
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")

def enter_move(board):
    user_move = input("Enter a move:")
    try:
        user_move= int(user_move)
    except ValueError:
        user_move = int(input("Enter a move:"))

    row_index = 0
    cell_index = 0
    for row in board:
        for cell in row:
            if cell == user_move:
                board[row_index][cell_index] = "O"
            cell_index += 1
        row_index += 1
        cell_index = 0


def free_squares(board):
    free_list = []
    row_index = 0
    cell_index = 0
    for row in board:
        for cell in row:
            if type(cell) == type(1):
                free_list.append((row_index,cell_index))
            cell_index += 1
        row_index += 1
        cell_index = 0
    return free_list

def draw_move(board):
    free_cells = free_squares(board)
    index = rd.randrange(len(free_cells))
    move = free_cells[index]
    board[move[0]][move[1]] = "X"
    print(f"Computer moved {move[0], move[1]}")

def victory(board, sign):
    
    #Rows 
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign):
        print(f"{sign} has won")
        return True
    
    elif (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign):
        print(f"{sign} has won")
        return True
    
    elif (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign):
        print(f"{sign} has won")
        return True

    #Columns
    elif (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign):
        print(f"{sign} has won")
        return True
    
    elif (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign):
        print(f"{sign} has won")
        return True
    
    elif (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
        print(f"{sign} has won")
        return True

    #Diagonals
    elif (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):
        print(f"{sign} has won")
        return True
    
    elif (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        print(f"{sign} has won")
        return True
    
initial = True
while True:
    if initial:
        print_board(board)
        initial = False    
    enter_move(board)
    player_win = victory(board, "O")
    if player_win or len(free_squares(board)) == 0:
        print("Game over")
        break
    print_board(board)
    draw_move(board)
    computer_win = victory(board, "X")
    if computer_win or len(free_squares(board)) == 0:
        print("Game over")
        break
    print_board(board)
