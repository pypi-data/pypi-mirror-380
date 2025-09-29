import chess
from oralchess import minimax

def test_minimax_startpos():
    """Test basic minimax run from starting position"""
    board = chess.Board()
    score, move = minimax(board, depth=2, alpha=-9999, beta=9999, is_maximizing=True)

    # Harus ada langkah yang valid
    assert move is not None, "Minimax should return a move"
    assert board.is_legal(move), f"Move {move} should be legal from start position"

def test_minimax_after_move():
    """Test minimax after one move"""
    board = chess.Board()
    board.push_uci("e2e4")  # Putih jalan
    score, move = minimax(board, depth=2, alpha=-9999, beta=9999, is_maximizing=False)

    # Harus ada langkah hitam yang valid
    assert move is not None, "Engine should suggest a move for black"
    assert board.is_legal(move), f"Move {move} should be legal for black"

def test_minimax_checkmate():
    """Test minimax detects checkmate correctly"""
    # Fool's mate posisi
    board = chess.Board("rnb1kbnr/pppp1ppp/8/4p3/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 0 3")
    score, move = minimax(board, depth=2, alpha=-9999, beta=9999, is_maximizing=True)

    # Skor harus negatif besar (karena putih kalah)
    assert score < -9000, f"Expected losing score, got {score}"
