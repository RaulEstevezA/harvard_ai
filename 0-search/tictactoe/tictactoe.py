"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


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

    # count all 'X' and 'O' marks on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    # if counts are equal, it's X's turn; otherwise, it's O's turn
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # return a set of all options
    return {(x, y) for x, row  in enumerate(board) for y, cell in enumerate(row) if cell == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # create a clone of the board to avoid mutating the original
    move_board = copy.deepcopy(board)

    # assign player's move in the board
    move_board[action[0]][action[1]] = player(board)

    return move_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # possible winning combinations: rows, columns, and diagonals
    winning_combinations = [
        # rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        # columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        # diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    # check is there are any combination
    for combo in winning_combinations:
        a, b, c = combo
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] and board[a[0]][a[1]] is not EMPTY:
            return board[a[0]][a[1]]
    
    # else return none
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check winner
    if winner(board) is not None:
        return True
    
    # check any free box
    if any(EMPTY in row for row in board):
        return False

    # else finish the game
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    # return 1 if X is the winner
    if winner(board) == X:
        return 1
    
    # return -1 if O is the winner
    elif winner(board) == O:
        return -1
    
    # retunr 0 if tie
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # determine current player
    actual_player = player(board)

    # initialize best move
    next_move = None
    
    # if X plays (maximizing player)
    if actual_player == X:
        best_score = float('-inf')
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_score:
                best_score = value
                next_move = action
    
    # if O plays (minimizing player)
    else:
        best_score = float('inf')
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_score:
                best_score = value
                next_move = action

    # return next move
    return next_move
    

def max_value(board):
    """
    Returns the maximum value that can get from this board.
    """

    # if game ended, return the utility
    if terminal(board):
        return utility(board)

    # we initialize it with the lowest possible value  
    value = float('-inf')  


    # we calculate the minimum value that the opponent would obtain if we do this action
    for action in actions(board):
        value = max(value, min_value(result(board, action)))

    # return the value
    return value


def min_value(board):
    """
    Returns the minimum value that can get from this board.
    """
    
    # if game ended, return the utility
    if terminal(board):
        return utility(board)
    

    # we initialize it with the lowest possible value  
    value = float('inf')  


    # we calculate the minimum value that the opponent would obtain if we do this action
    for action in actions(board):
        value = min(value, max_value(result(board, action)))

    # return the value
    return value

