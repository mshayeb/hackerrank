#!/usr/bin/python

# Head ends here
import os
def next_move(posx, posy, board):    
    if os.path.exists("kb.txt"):
        save = open("kb.txt", "r")
        #skip to current row
        for i in range(posx):
            save.readline()        
        row = save.readline()
        #load this line and next line (if possible)
        for i in range(2 - (posx == len(board) - 1)):        
            for j in range(5):
                if row[j] != "o" and board[posx + i][j] == "o":
                    board[posx + i][j] = row[j]

    if posx == 0 and posy == 3:
        print "kb (before):"
        save.seek(0, 0)
        print save.read()
        print "board (before):"
        for row in board:
            print "".join(row)
                    
    #save whole thing
    save = open("kb.txt", "w+")
    new = ""
    for row in board:
        new += "".join(row) + "\n"
    save.write(new) 
    if posx == 0 and posy == 3:
        print "kb (after):"
        save.seek(0, 0)
        print save.read()
        print "board (after):"
        for row in board:
            print "".join(row)
    save.close()
    #decision-making time
    if "d" in board[posx]:
        dY = board[posx].index("d")        
        if dY == posy:
            print "CLEAN"
        elif dY < posy:
            print "LEFT"
        else:
            print "RIGHT"
    elif "o" in board[posx]:
        oY = board[posx].index("o")     
        if oY < posy:
            print "LEFT"
        else:
            print "RIGHT"
    else:
        print "DOWN"

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
