"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


class State():
    def __init__(self, board, parent, actions, exploredActions, depth):
        self.board = board
        self.parent = parent
        self.actions = actions
        self.exploredActions = exploredActions
        self.depth = depth


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
#    raise NotImplementedError
    numberOfX = 0
    numberOfO = 0    

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numberOfX+=1
            if board[i][j] == O:
                numberOfO+=1
    
    # it's O's turn if there are more X than O on the boars
    if numberOfX > numberOfO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
#    raise NotImplementedError

    possiblesActions = []    

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possiblesActions.append((i,j))
    
    return possiblesActions
                


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
#    raise NotImplementedError
    
#    newBoard = copy.copy(board)
    newBoard = copy.deepcopy(board)
    
    for i in range(3):
        for j in range(3):
            if action == (i,j):
                # valid action
                if newBoard[i][j] == EMPTY:
                    newBoard[i][j] = player(board)
                # action not valid 
                else:
                  raise NotImplementedError     
    return newBoard
    


def computeWinner(board, p):
    """
    For a given player, returns True if he won and False otherwise
    Is called inside winner(board)
    """
    
    result = False
    
    if board[0][0] == p:
        if board[0][1] == p:
            if board[0][2] == p:
                result = True
        if board[1][0] == p:
            if board[2][0] == p:
                result = True
        if board[1][1] == p:
            if board[2][2] == p:
                result = True
    
    if board[0][2] == p:
        if board[1][1] == p:
            if board[2][0] == p:
                result = True
        if board[1][2] == p:
            if board[2][2] == p:
                result = True
                
    if board[0][1] == p:
        if board[1][1] == p:
            if board[2][1] == p:
                result = True
                
    if board[1][0] == p:
        if board[1][1] == p:
            if board[1][2] == p:
                result = True
                
    if board[2][0] == p:
        if board[2][1] == p:
            if board[2][2] == p:
                result = True
                
    return result
                
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
#    raise NotImplementedError
    whoIsWinner = None

    if computeWinner(board, X):
        whoIsWinner = X
    if computeWinner(board, O):
        whoIsWinner = O
        
    return whoIsWinner
    
    
    # countX = 0
    
    # for i in range(3):
    #     if board[i][0] == X:
    #         countX+=1
            
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
#    raise NotImplementedError
    isGameOver = False
        
    countFilledCases = 0
    
    # if no more emply case, the game is over
    for i in range(3):
        for j in range(3):
            if board[i][j] == X or board[i][j] == O:
                countFilledCases+=1
    
    if countFilledCases == 9:
        isGameOver = True
        
    # if there is a winner, the game is over
    if winner(board):
        isGameOver = True
    
    return isGameOver


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
#    raise NotImplementedError
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def randomPlay(board):
    """
    Returns a random play by the AI
    """
    ai_has_played = False
    
    while ai_has_played == False:
            i_choice = random.randint(0, 2)
            j_choice = random.randint(0, 2)
            
            if board[i_choice][j_choice] == EMPTY:
                ai_has_played = True
                return (i_choice, j_choice)
      

def maxValue(board):
    v = -1000
    if terminal(board):
        return utility(board)
    
    # return the max value of all the possible actions
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    
    return v
        

def minValue(board):
    v = +1000
    if terminal(board):
        return utility(board)
    
    # return the min value of all the possible actions
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
        
    return v        


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
#   The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
#   The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).

    highestValue = -100
    lowestValue = 100
    optimalAction = (0,0)
    
    # if AI plays X, it is the maximizing player
    # if AI plays first, we force him to place the first X in the middle
    # indeed, for the AI, on the 1st turn, all possibilities have the same score
    # so it chose the last square (2,2)
    # we want it to chose (1,1) instead
    # first, let's see if it is the first turn
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count+=1

    
    if player(board) == X:
        # if 9 EMPTY, it's the 1st turn
        if count == 9:
            print("return (1,1)")
            return (1,1)
        print("AI plays X")
        for action in actions(board):
            if minValue(result(board, action)) >= highestValue:
                highestValue = minValue(result(board, action))
                print("highest value = ", highestValue, end = '')
                print(" for action = ", action)
                optimalAction = action
                print("optimalAction is now ", optimalAction)
    # if AI plays O, it is the minimizing player
    elif player(board) == O:
        print("AI plays O")
        for action in actions(board):
            if maxValue(result(board, action)) <= lowestValue:
                lowestValue = maxValue(result(board, action))
                print("lowest value = ", lowestValue, end = '')
                print(" for action = ", action)                
                optimalAction = action
                print("optimalAction is now ", optimalAction)
     
    print("optimal action is :", optimalAction)
    return optimalAction

#   raise NotImplementedError
