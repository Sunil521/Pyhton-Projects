board_size = 8
BLACK,WHITE,EMPTY = 'B','W','_'
offsets = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
def inverse(piece):
    if piece == BLACK:
        return WHITE 
    else:
        return BLACK
def main():
    board = create_board()
    piece = BLACK
    while has_valid_move(board, piece):
        game_loop(board, piece)
        if has_valid_move(board, inverse(piece)):
            piece = inverse(piece)
    print_board(board)
    black, white = 0,0
    for row in board:
        for token in row:
            if token is WHITE: white += 1
            if token is BLACK: black += 1
    if black == white:
        print("It's a tie!")
    else:
        print()
        print('{token} is the winner!' %s (BLACK if black>white else WHITE))
    return
def create_board():
    board = [[EMPTY for x in range(board_size)] for x in range(board_size)]
    half = board_size//2
    board[half-1][half-1] = WHITE
    board[half][half] = WHITE
    board[half-1][half] = BLACK
    board[half][half-1] = BLACK
    return board
def print_board(board):
    for row in range(len(board)):
        print(*board[row], sep='  ')
    return
print (int(input("enter number of games")))
def game_loop(board, piece):
    print()
    print_board(board)
    while(True):
        try:
            move = eval(input('enter row and column of %s  ' % piece))
            move = tuple(reversed(move))
            if is_valid_move(board, piece, move):
                place_piece(board, piece, move)
                return
            else:
                raise AssertionError
        except (TypeError, ValueError, IndexError, SyntaxError, AssertionError):
            print('Invalid move. Try again.')

def is_valid_move(board, piece, move):
    if board[move[0]][move[1]] is not EMPTY:
        return False
    for offset in offsets:
        check = [move[0]+offset[0], move[1]+offset[1]]
        while 0<=check[0]<board_size-1 and 0<=check[1]<board_size-1 and     board[check[0]][check[1]] is inverse(piece):
            check[0] += offset[0]
            check[1] += offset[1]
            if board[check[0]][check[1]] is piece:
                return True
    return False
def place_piece(board, piece, move):
    board[move[0]][move[1]] = piece
    for offset in offsets:
        check = [move[0]+offset[0], move[1]+offset[1]]
        while 0<=check[0]<board_size and 0<=check[1]<board_size:
            if board[check[0]][check[1]] is EMPTY: break
            if board[check[0]][check[1]] is piece:
                flip(board, piece, move, offset)
                break
            check[0] += offset[0]
            check[1] += offset[1]
    return
def flip(board, piece, move, offset):
    check = [move[0]+offset[0], move[1]+offset[1]]
    while(board[check[0]][check[1]] is inverse(piece)):
        board[check[0]][check[1]] = piece
        check[0] += offset[0]
        check[1] += offset[1]
    return
def has_valid_move(board, piece):
    for y in range(board_size):
        for x in range(board_size):
            if is_valid_move(board, piece, (y,x)): return True
    return False
main()

