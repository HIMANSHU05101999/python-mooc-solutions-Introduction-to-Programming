# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    #game_board[y][x]=piece
    for row in range (len(game_board)):
        for col in range (len(game_board[row])):
            if col==x and row==y:
                if game_board[y][x]=="":
                    game_board[y][x]=piece
                    return True
                else:
                    return False
    return False

if __name__=="__main__":
    game_board = [['', 'O', ''], ['', '', ''], ['O', 'O', 'O']] 
    print(play_turn(game_board, 1, 1, "O"))
    print(game_board)