import random

def draw_board(board):
    print('-------------')
    for row in range(3):
        print('|', end='')
        for col in range(3):
            print(f' {board[row][col]} |', end='')
        print('\n-------------')

def check_win(board, player):
    # Check rows
    for row in range(3):
        if all(cell == player for cell in board[row]):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

def player_move(board):
    while True:
        try:
            row = int(input('Enter row (0, 1, or 2): '))
            col = int(input('Enter column (0, 1, or 2): '))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print('Invalid move. Try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def computer_move(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True

    while True:
        draw_board(board)

        if player_turn:
            player_move(board)
        else:
            computer_move(board)

        if check_win(board, 'X'):
            draw_board(board)
            print('You win!')
            break
        elif check_win(board, 'O'):
            draw_board(board)
            print('Computer wins!')
            break
        elif check_tie(board):
            draw_board(board)
            print('It\'s a tie!')
            break

        player_turn = not player_turn

if __name__ == '__main__':
    main()
