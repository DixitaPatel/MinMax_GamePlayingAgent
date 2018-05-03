import copy
import time

#printing game board
def printboard(gameboard):
    import numpy as np
    print(np.matrix(gameboard))

#checking selected move
def printmove(movenum):
    print movenum

#writing selected move and board state after performing that move into the output file
def outputwrite(firstline, middleboard):
    outputfile.write('%s' % chr(int(firstline[1]) + 65))
    outputfile.write('%s' % str(firstline[0] + 1))
    outputfile.write("\n")
    for i in range(0, n):
        for j in range(0, n):
            outputfile.write(middleboard[i][j])
        outputfile.write("\n")


#selecting the move
def selectmove(gameboard, movenum, move):
    if move in movenum:
        for values in movenum[move]:
            gameboard[values[0]][values[1]] = "*"

    # printboard(gameboard)
    for col in range(0, n):
        for k in range(0, n):
            for row in range(n - 1, 0, -1):
                if gameboard[row - 1][col] != "*" and gameboard[row][col] == "*":
                    temp = gameboard[row][col]
                    gameboard[row][col] = gameboard[row - 1][col]
                    gameboard[row - 1][col] = temp
    # printboard(gameboard)
    return gameboard


#creating box of all the connected similar kind of fruits
def createbox(gameboard):
    movenum = {}
    tempboard = []
    templist = []
    move = 0
    # --------------Last row-----------------------------------
    if gameboard[n - 1][0] == "*":
        templist.append('*')
    else:
        move = move + 1
        templist.append(move)
        movenum.setdefault(str(move), []).append((n - 1, 0))
    for j in range(1, n):
        if gameboard[n - 1][j] == '*':
            templist.append('*')
        elif gameboard[n - 1][j] == gameboard[n - 1][j - 1]:
            templist.append(templist[-1])
            movenum.setdefault(str(move), []).append((n - 1, j))
        else:
            move = move + 1
            templist.append(move)
            movenum.setdefault(str(move), []).append((n - 1, j))
    tempboard.append(templist)
    # print tempboard

    # ---------------------------------------------------
    for i in range(n - 2, -1, -1):
        newtemplist = []
        for j in range(0, n):
            if gameboard[i][j] == '*':
                newtemplist.append('*')
                continue

            else:
                if gameboard[i][j] == gameboard[i][j - 1] and gameboard[i][j] == gameboard[i + 1][j]:
                    newtemplist.append(tempboard[0][j])
                    movenum.setdefault(str(tempboard[0][j]), []).append((i, j))
                    extra = copy.deepcopy(newtemplist)
                    for x in range(j - 1, -1, -1):
                        if x == 0:
                            new = movenum[str(newtemplist[x])].pop()
                            newtemplist[x] = newtemplist[-1]
                            movenum.setdefault(str(newtemplist[x]), []).append(new)
                            break
                        elif newtemplist[x] == extra[x - 1] and newtemplist[x] is not "*":
                            new = movenum[str(newtemplist[x])].pop()
                            newtemplist[x] = newtemplist[-1]
                            movenum.setdefault(str(newtemplist[x]), []).append(new)
                        else:
                            new = movenum[str(newtemplist[x])].pop()
                            newtemplist[x] = newtemplist[-1]
                            movenum.setdefault(str(newtemplist[x]), []).append(new)
                            break

                elif gameboard[i][j] == gameboard[i + 1][j]:
                    newtemplist.append(tempboard[0][j])
                    movenum.setdefault(str(tempboard[0][j]), []).append((i, j))
                elif j != 0:
                    if gameboard[i][j] == gameboard[i][j - 1]:
                        newtemplist.append(newtemplist[-1])
                        movenum.setdefault(str(newtemplist[-1]), []).append((i, j))
                    else:
                        move = move + 1
                        newtemplist.append(move)
                        movenum.setdefault(str(move), []).append((i, j))
                else:
                    move = move + 1
                    newtemplist.append(move)
                    movenum.setdefault(str(move), []).append((i, j))
        tempboard.insert(0, newtemplist)
    for col in range(0, n):
        for row in range(0, n - 1):
            if gameboard[row][col] == gameboard[row + 1][col] and gameboard[i][j] is not "*":
                tempboard[row + 1][col] = tempboard[row][col]
    for row in range(0, n):
        for col in range(n - 1, -1, -1):
            if gameboard[row][col] == gameboard[row][col - 1] and gameboard[i][j] is not "*":
                tempboard[row][col - 1] = tempboard[row][col]
                # printmove(movenum)
                # print "+++++++++++++++++++++++++++++++++++++"
                # for line in tempboard:
                #       print line
                # ---------- print tempgameboard ---------
                # printboard(tempboard)
                # ----------------------------------

    return movenum



#max player
def maxplayer(gameboard, alpha, beta, depth):
    midtime = time.time() - starttime
    movenum = createbox(gameboard)
    if depth == 3 or (midtime < (t-10)):
        length = 0
        for move in movenum:
            l = movenum[move]
            if len(l) > length:
                lenght = len(l)
        return lenght
    if len(movenum.keys()) == 1:
        for move in movenum:
            l = movenum[move]
        # print "--------------------"
        # print len(l)
        return len(l)
    moves = movenum.keys()
    # firstmove = moves[0]
    for move in moves:
        newboard = copy.deepcopy(gameboard)
        middleboard = selectmove(newboard, movenum, move)
        score = minplayer(middleboard, alpha, beta, depth + 1)
        alpha = max(alpha, score)
        if beta <= alpha:
            # firstmove = move
            return beta
    return alpha

#min player
def minplayer(gameboard, alpha, beta, depth):
    midtime = time.time() - starttime
    movenum = createbox(gameboard)
    if depth == 3 or (midtime < (t-10)):
        length = 0
        for move in movenum:
            l = movenum[move]
            if len(l) > length:
                length = len(l)
        return length
    if len(movenum.keys()) == 1:
        for move in movenum:
            l = movenum[move]
        return len(l)
    moves = movenum.keys()
    # firstmove = moves[0]
    #fscore = float('inf')
    for move in moves:
        newboard = copy.deepcopy(gameboard)
        middleboard = selectmove(newboard, movenum, move)
        score = maxplayer(middleboard, alpha, beta, depth + 1)
       # beta = min(beta, score)
        if score <= alpha:
            # firstmove = move
            return alpha
        if score < beta:
            beta = score
    return beta

#minmax with alpha-beta prunning to maximize the score
def minmax(gameboard, alpha, beta, depth):
    movenum = createbox(gameboard)
    moves = movenum.keys()
    firstmove = moves[0]
    fscore = float('-inf')
    for move in moves:
        newboard = copy.deepcopy(gameboard)
        middleboard = selectmove(newboard, movenum, move)
        score = minplayer(middleboard, alpha, beta, depth)
        if score > fscore:
            firstmove = move
            fscore = score
    return firstmove


starttime = time.time()                                 #time variable to keep track of time left while playing
file = open("input.txt", "r")
outputfile = open("output.txt", "w")
n = int(file.readline()) # n*n matrix board
# print n
p = int(file.readline()) # types of fruits
# print p
t = float(file.readline()) # time left to complete game
# print t

gameboard = []

for i in range(n):
    line = [char for char in file.readline().rstrip("\n")]
    gameboard.append(line)

originalboard = copy.deepcopy(gameboard)
# printboard(gameboard)
movenum = createbox(originalboard)

if t > 10:
    x = minmax(gameboard, float('-inf'), float('inf'), 0)
else:
    a = movenum.keys()
    x = a[0]
# print x

middleboard = selectmove(originalboard, movenum, x)
firstline = movenum[x][0]
outputwrite(firstline, middleboard)
# selectmove(gameboard, movenum, str(2))
