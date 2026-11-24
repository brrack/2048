import random

def UpdateBoard(input):
    if input == "w":
        for i in range(len(board)):
            if board[i] == "_":
                continue
            else:
                if i >= 4 and board[i-4] == "_":
                    if i >= 8 and board[i-8] == "_":
                        if i >= 12 and board[i-12] == "_":
                            board[i-12] = board[i]
                        elif i >= 12 and board[i-12] == board[i]:
                            board[i-12] = 2 * board[i]
                        else:
                            board[i-8] = board[i]
                    elif i >= 8 and board[i-8] == board[i]:
                        board[i-8] = 2 * board[i]
                    else:
                        board[i-4] = board[i]
                    
                    board[i] = "_"
                elif i >= 4 and board[i-4] == board[i]:
                    board[i-4] = 2 * board[i]
                    board[i] = "_"
                else:
                    continue

    elif input == "a":
        for i in range(len(board)):
            if board[i] == "_":
                continue
            else:
                if i != 0 and i != 4 and i != 8 and i != 12 and board[i-1] == "_":
                    if i-1 != 0 and i-1 != 4 and i-1 != 8 and i-1 != 12 and board[i-2] == "_":
                        if i-2 != 0 and i-2 != 4 and i-2 != 8 and i-2 != 12 and board[i-3] == "_":
                            board[i-3] = board[i]
                        elif i-2 != 0 and i-2 != 4 and i-2 != 8 and i-2 != 12 and board[i-3] == board[i]:
                            board[i-3] = 2 * board[i]
                        else:
                            board[i-2] = board[i]
                    elif i-1 != 0 and i-1 != 4 and i-1 != 8 and i-1 != 12 and board[i-2] == board[i]:
                        board[i-2] = 2 * board[i]
                    else:
                        board[i-1] = board[i]
                            
                    board[i] = "_"
                elif i != 0 and i != 4 and i != 8 and i != 12 and board[i-1] == board[i]:
                    board[i-1] = 2 * board[i]
                else:
                    continue
    elif input == "s":
        for i in range(len(board) - 1, -1, -1):
            if board[i] == "_":
                continue
            else:
                if i <= 11 and board[i+4] == "_":
                    if i <= 7 and board[i+8] == "_":
                        if i <= 3 and board[i+12] == "_":
                            board[i+12] = board[i]
                        elif i <= 3 and board[i+12] == board[i]:
                            board[i+12] = 2 * board[i]
                        else:
                            board[i+8] = board[i]
                    elif i <= 7 and board[i+8] == board[i]:
                        board[i+8] = 2 * board[i]
                    else:
                        board[i+4] = board[i]
                    
                    board[i] = "_"
                elif i <= 11 and board[i+4] == board[i]:
                    board[i+4] = 2 * board[i]
                    board[i] = "_"
                else:
                    continue

    elif input == "d":
        for i in range(len(board) - 1, -1, -1):
            if board[i] == "_":
                continue
            else:
                if i != 3 and i != 7 and i != 11 and i != 15 and board[i+1] == "_":
                    if i+1 != 3 and i+1 != 7 and i+1 != 11 and i+1 != 15 and board[i+2] == "_":
                        if i+2 != 3 and i+2 != 7 and i+2 != 11 and i+2 != 15 and board[i+3] == "_":
                            board[i+3] = board[i]
                        elif i+2 != 3 and i+2 != 7 and i+2 != 11 and i+2 != 15 and board[i+3] == board[i]:
                            board[i+3] = 2 * board[i]
                        else:
                            board[i+2] = board[i]
                    elif i+1 != 3 and i+1 != 7 and i+1 != 11 and i+1 != 15 and board[i+2] == board[i]:
                        board[i+2] = 2 * board[i]
                    else:
                        board[i+1] = board[i]
                                    
                    board[i] = "_"
                elif i != 3 and i != 7 and i != 11 and i != 15 and board[i+1] == board[i]:
                    board[i+1] = 2 * board[i]
                else:
                    continue

    PrintBoard()

def NewNum():
    global board
    newnum = random.randint(0, 15)
    newval = random.choice([2, 4])
    
    if board[newnum] == "_":
        board[newnum] = newval
    else:
        NewNum()

def PrintBoard():
    global board
    NewNum()
    print(board[0], board[1], board[2], board[3])
    print(board[4], board[5], board[6], board[7])
    print(board[8], board[9], board[10], board[11])
    print(board[12], board[13], board[14], board[15])
    print("------------------------------")


board = ["_", "_", "_", "_",
         "_", "_", "_", "_",
         "_", "_", "_", "_",
         "_", "_", "_", "_"]

NewNum()
PrintBoard()

while True:
    player_input = input()
    UpdateBoard(player_input)