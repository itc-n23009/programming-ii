def is_valid_chess_board(board):
    valid_positions = {f"{file}{rank}" for file in "abcdefgh" for rank in "12345678"}
    valid_pieces = {'king', 'queen', 'rook', 'bishop', 'knight', 'pawn'}
    piece_count = {piece: 0 for piece in (f'{color}{name}' for color in 'wb' for name in valid_pieces)}

    for position, piece in board.items():
        if position not in valid_positions or len(piece) < 5 or piece[0] not in 'wb' or piece[1:] not in valid_pieces:
            return False
        piece_count[piece] += 1

    return (
        piece_count['wking'] == 1 and piece_count['bking'] == 1 and
        sum(piece_count[piece] for piece in piece_count if piece.startswith('w')) <= 16 and
        sum(piece_count[piece] for piece in piece_count if piece.startswith('b')) <= 16 and
        piece_count['wpawn'] <= 8 and piece_count['bpawn'] <= 8
    )

chess_board = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'
}

print(is_valid_chess_board(chess_board))
