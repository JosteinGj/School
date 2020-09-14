def make_board(board_string):
    board=[]
    board_string=list(board_string)
    for pos,val in enumerate(board_string):
        if val == ".":
            board_string[pos]=None
    for i in range(0,len(board_string),8):
        board.append(list(board_string[i:i+8]))
    return board
boardstring="RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
board1=make_board("RNBQKBNRPPPPPPPP................................pppppppprnbkqbnr")
def getpeice(board,row, column):
    return board[row][column]
def get_legal_moves(board,row,column):
    peice=getpeice(board,row,column)
    ptype=None
    pos=[row,column]
    if ord(peice)>91:
        ptype="black"
    else:
        ptype="white"
    if peice.lower()=="p":
        if board[row+1][column]!=None:
            if pos==[1,column]:
                return [(row+1,column),(row+2,column)]
            else:
                return 





#hvis hvit




