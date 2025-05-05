"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = 0
    o_count = 0
    
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    # o 'O' só deve jogar se o n de 'X' for maior que o n de 'O', caso sejam iguais ou n de 'O' for maior que n de 'X' é a vez do 'X' jogar
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(len(board)): # acessa os indices de i: [0][1][2]
        for j in range(len(board[i])): # acessa os indices de j: [0][1][2]
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))    

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # Verifica se a ação está dentro dos limites do tabuleiro
    if i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception("Invalid action: position out of bounds.")

    if board[i][j] != EMPTY:
        raise Exception ("Invalid action: cell is not empty.")   

    new_board = copy.deepcopy(board)

    # new_board pega o valor (X ou O) de player(board), pq ele vai calcular de quem é o proximo turno, e a jogada em si (as coordenadas de X ou O) vai ser determinada por action
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # horizontal
    for row in board:
        if row[0] == row[1] == row[2] == X:
            return X 
        if row[0] == row[1] == row[2] == O:
            return O 

    # vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == X:
            return X 
        if board[0][col] == board[1][col] == board[2][col] == O:
            return O 
    
    # diagonal principal
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X 
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O 

    #diagonal secundaria
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # verifica se alguem ganhou
    vencedor = winner(board)
    if vencedor != None:
        return True
    
    count_empty = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                count_empty += 1
    
    if count_empty == 0:
        return True
    else: 
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == X:
        return 1
    elif result == O:
        return -1
    else: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_score = float("-inf")
        best_move = None

        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_move = action
    
    else:
        best_score = float("inf")
        best_move = None

        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_move = action

    return best_move

def max_value(board):
    v = float("-inf")

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v

def min_value(board):
    v = float ("inf")

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v