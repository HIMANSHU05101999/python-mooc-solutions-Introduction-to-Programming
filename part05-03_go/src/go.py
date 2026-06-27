# Write your solution here

def who_won(game_board: list):
    player=[0,0]
    for i in range (0,len(game_board)):
        for j in range (0,len(game_board[i])):
            if game_board[i][j]==1:
                player[0]+=1
            elif game_board[i][j]==2:
                player[1]+=1
    if player[0]>player[1]:
        return 1
    elif player[1]>player[0]:
        return 2
    else:
        return 0


if __name__=="__main__":
    m = [[1, 2, 0], [0, 1, 1], [2, 0, 0]]
    print(who_won(m))
    