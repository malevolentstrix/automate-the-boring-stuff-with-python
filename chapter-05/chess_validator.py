# TODO - INCOMPLETE
# PRACTICE PROJECT "Chess Dictionary Validator" OF CHAPTER - 5
# BY JITHIN JOHN
board = {'1a': 'wrook','1b':'wknight','1c':'wbishop','1d':'wqueen','1e':'wking','1f':'wbishop','1g':'wknight','1h':'wrook',
'2a':'wpawn','2b':'wpawn','2c':'wpawn','2d':'wpawn','2e':'wpawn','2f':'wpawn','2g':'wpawn','2h':'wpawn',
'3a':'','3b':'','3c':'','3d':'','3e':'','3f':'','3g':'','3h':'',
'4a':'','4b':'','4c':'','4d':'','4e':'','4f':'','4g':'','4h':'',
'5a':'','5b':'','5c':'','5d':'','5e':'','5f':'','5g':'','5h':'',
'6a':'','6b':'','6c':'','6d':'','6e':'','6f':'','6g':'','6h':'',
'7a':'bpawn','7b':'bpawn','7c':'bpawn','7d':'bpawn','7e':'bpawn','7f':'bpawn','7g':'bpawn','7h':'bpawn',
'8a':'brook','8b':'bknight','8c':'bbishop','8d':'bqueen','8e':'bking','8f':'bbishop','8g':'bknight','8h':'brook'}

def isValidChessBoard(boardasdictionary):
    total_pieces = 0
    i = 0
    for i in boardasdictionary.values():
        if i != '':
            total_pieces = total_pieces + 1
    if total_pieces != 32:
        return 'The Chessboard is not valid according to the given data'

    black_pawn = 0
    white_pawn = 0
    i = 0
    for i in boardasdictionary.values():
        if i == 'bpawn':
            black_pawn = black_pawn + 1
        if i == 'wpawn':
            white_pawn = white_pawn + 1
    if white_pawn != 8 or black_pawn != 8:
        return 'The Chessboard is not valid according to the given data'

    black_king=0
    white_king=0
    i = 0
    for i in boardasdictionary.values():
        if i == 'bking':
            black_king = black_king + 1
        if i == 'wking':
           white_king = white_king + 1
    if black_king != 1 or white_king != 1:
        return 'The Chessboard is not valid according to the given data'

    valid_spaces = {'1a','1b','1c','1d','1e','1f','1g','1h',
                    '2a','2b','2c','2d','2e','2f','2g','2h',
                    '3a','3b','3c','3d','3e','3f','3g','3h',
                    '4a','4b','4c','4d','4e','4f','4g','4h',
                    '5a','5b','5c','5d','5e','5f','5g','5h',
                    '6a','6b','6c','6d','6e','6f','6g','6h',
                    '7a','7b','7c','7d','7e','7f','7g','7h',
                    '8a','8b','8c','8d','8e','8f','8g','8h'}

    for i in boardasdictionary.keys():
        if valid_spaces(i) != i
        return 'The Chessboard is not valid according to the given data'
    return 'The Chessboard is valid according to the given data'

print(isValidChessBoard(board))