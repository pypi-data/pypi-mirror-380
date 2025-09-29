# calculator_faster_chess.py
import os
import chess
import chess.polyglot
import math
import random
from cerebras.cloud.sdk import Cerebras

# ==================================
# Konfigurasi Cerebras AI
# ==================================
API_KEY = "csk-9896dpfjmmtmx35dy8frew2t6rvkjht5h6wj8hnh9p6j4h5r"

client = Cerebras(api_key=API_KEY)

# ==================================
# Piece Square Tables (bonus posisi)
# ==================================
PIECE_SQUARE_TABLES = {
    chess.PAWN: [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, -20, -20, 10, 10, 5,
        5, -5, -10, 0, 0, -10, -5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, 5, 10, 25, 25, 10, 5, 5,
        10, 10, 20, 30, 30, 20, 10, 10,
        50, 50, 50, 50, 50, 50, 50, 50,
        0, 0, 0, 0, 0, 0, 0, 0,
    ],
    chess.KNIGHT: [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50,
    ],
    chess.BISHOP: [
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -20,-10,-10,-10,-10,-10,-10,-20,
    ],
    chess.ROOK: [
        0, 0, 5, 10, 10, 5, 0, 0,
        0, 0, 5, 10, 10, 5, 0, 0,
        0, 0, 5, 10, 10, 5, 0, 0,
        0, 0, 5, 10, 10, 5, 0, 0,
        0, 0, 5, 10, 10, 5, 0, 0,
        0, 0, 5, 10, 10, 5, 0, 0,
        25,25,25,25,25,25,25,25,
        0, 0, 5, 10, 10, 5, 0, 0,
    ],
    chess.QUEEN: [
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
        -5,   0,  5,  5,  5,  5,  0, -5,
        0,    0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20,
    ],
    chess.KING: [
        20, 30, 10, 0, 0, 10, 30, 20,
        20, 20, 0, 0, 0, 0, 20, 20,
        -10,-20,-20,-20,-20,-20,-20,-10,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
    ]
}

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

# ==================================
# Evaluasi Posisi
# ==================================
def evaluate_board(board: chess.Board):
    if board.is_checkmate():
        if board.turn:
            return -999999
        else:
            return 999999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    eval_score = 0
    for piece_type in PIECE_VALUES.keys():
        for square in board.pieces(piece_type, chess.WHITE):
            eval_score += PIECE_VALUES[piece_type]
            eval_score += PIECE_SQUARE_TABLES[piece_type][square]
        for square in board.pieces(piece_type, chess.BLACK):
            eval_score -= PIECE_VALUES[piece_type]
            eval_score -= PIECE_SQUARE_TABLES[piece_type][chess.square_mirror(square)]

    # mobility
    eval_score += len(list(board.legal_moves)) * (10 if board.turn else -10)

    return eval_score

# ==================================
# Minimax + Alpha-Beta
# ==================================
def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    if is_maximizing:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

# ==================================
# Fungsi Hybrid dengan Cerebras
# ==================================
def analyze_with_cerebras(board: chess.Board, depth: int = 3):
    score, best_move = minimax(board, depth, -math.inf, math.inf, board.turn)
    board_fen = board.fen()

    # kirim ke Cerebras untuk insting strategi
    query = f"""
You are a chess grandmaster AI.
The current board state (FEN): {board_fen}
Candidate best move (engine): {best_move}

ONLY reply with the best move (like e4) and the opening name in one line below.
No extra explanation.
"""


    stream = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a chess analysis assistant."},
            {"role": "user", "content": query}
        ],
        model="qwen-3-235b-a22b-instruct-2507",
        stream=True,
        max_completion_tokens=500,
        temperature=0.7,
        top_p=0.9
    )

    ai_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            ai_response += chunk.choices[0].delta.content

    return best_move, score, ai_response
if __name__ == "__main__":
    board = chess.Board()  # papan awal
    best_move, score, ai_response = analyze_with_cerebras(board, depth=2)
    print("Best move:", best_move)
    print("Evaluation score:", score)
    print("AI Suggestion:\n", ai_response)

