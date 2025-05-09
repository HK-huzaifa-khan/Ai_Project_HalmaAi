from copy import deepcopy
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAX_TIME = 2.5  # Maximum seconds for AI to think 

def minimax(board, depth, alpha, beta, max_player, game, start_time):
    """Optimized minimax with alpha-beta pruning and time limit."""
    # Time cutoff check
    if time.time() - start_time > MAX_TIME:
        return board.evaluate(), None  

    if depth == 0 or board.winner() is not None:
        return board.evaluate(), board

    best_move = None
    moves = get_ordered_moves(board, WHITE if max_player else BLACK, game)

    if max_player:
        max_eval = float('-inf')
        for move in moves:
            eval, _ = minimax(move, depth-1, alpha, beta, False, game, start_time)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            eval, _ = minimax(move, depth-1, alpha, beta, True, game, start_time)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def get_ordered_moves(board, color, game):
    """Returns moves ordered by heuristic quality for better pruning."""
    moves = []
    for piece in board.get_all_pieces(color):
        for move in board.get_valid_moves(piece):
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board)
            moves.append((new_board.evaluate(), new_board))
    
    # Sort moves by evaluation (best first for WHITE, worst first for BLACK)
    moves.sort(key=lambda x: x[0], reverse=(color == WHITE))
    return [move[1] for move in moves]

def simulate_move(piece, move, board):
    """Optimized move simulation without deep copies."""
    board.move(piece, move[0], move[1])
    return board

def get_best_move(board, depth, game):
    """Entry point for AI move calculation with time limit."""
    start_time = time.time()
    _, best_move = minimax(board, depth, float('-inf'), float('inf'), True, game, start_time)
    return best_move or board  
